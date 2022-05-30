"""Set up the extension for running.

There are 4 stages for setup:

1. boot - called with the basic libraries.
2. with-screen - called when the screen is grabbed and the connection
    is established as a window manager.
3. pre-events - called after the screen is released, and before the event loop starts.
"""

from typing import Sequence, List, Tuple, Callable
from petronia_common.util import StdRet, UserMessage, RET_OK_NONE, collect_errors_from
from petronia_ext_lib.runner import LookupEventRegistryContext
from .configuration import ConfigurationStore
from .running_data import RunningData
from .hook_types import Hook, HookFactory, PhaseRunner


def start_server(
        context: LookupEventRegistryContext, config: ConfigurationStore,
        on_warning: Callable[[UserMessage], None],
        runner: PhaseRunner, hook_factories: Sequence[HookFactory],
) -> StdRet[Tuple[RunningData, Sequence[Hook]]]:
    """Start the connection to the X server, run the hooks, and start up the event loop."""

    # Step 1: boot
    boot_res = runner.boot(context, config)
    if boot_res.has_error:
        return boot_res.forward()

    # Step 2: After boot, run hooks.
    # Let all the hooks run before reporting an error.
    hook_boot_res: List[StdRet[None]] = []
    hooks: List[Hook] = []
    for hook_factory in hook_factories:
        hf_res = hook_factory(boot_res.result)
        if hf_res.has_error:
            hook_boot_res.append(hf_res.forward())
        else:
            hf_result = hf_res.result
            if isinstance(hf_result, UserMessage):
                on_warning(hf_result)
            else:
                assert isinstance(hf_result, Hook)  # nosec  # programmer checking
                hooks.append(hf_result)
    boot_errors = collect_errors_from(hook_boot_res)
    if boot_errors:
        return StdRet.pass_error(boot_errors)

    # Step 3: become the window manager
    wm_res = runner.become_window_manager(boot_res.result)
    if wm_res.has_error:
        return wm_res.forward()

    # Step 4: After becoming window manager, run hooks.
    hook_wm_res: List[StdRet[None]] = []
    for hook in hooks:
        hook_wm_res.append(hook.setup_wm_screen(wm_res.result))
    wm_errors = collect_errors_from(hook_wm_res)
    if wm_errors:
        return StdRet.pass_error(wm_errors)

    # Step 5: Get the event loop ready.
    evt_prep_res = runner.prepare_event_loop(wm_res.result)
    if evt_prep_res.has_error:
        return evt_prep_res.forward()

    # Step 6: before event loop runs, run hooks.
    hook_evt_res: List[StdRet[None]] = []
    for hook in hooks:
        hook_evt_res.append(hook.setup_pre_event_loop(evt_prep_res.result))
    evt_errors = collect_errors_from(hook_evt_res)
    if evt_errors:
        return StdRet.pass_error(evt_errors)

    # Step 7: run event loop and return.
    return runner.run_event_loop(evt_prep_res.result).map_static((evt_prep_res.result, hooks))


def stop_server(
        data: RunningData, timeout: float,
        runner: PhaseRunner, hooks: Sequence[Hook],
) -> StdRet[None]:
    """Stop the server."""
    # Run the hooks in reverse order.
    res: List[StdRet[None]] = []
    for i in range(len(hooks), 0, -1):
        res.append(hooks[i - 1].shutdown(data))

    # Finally, stop the server
    res.append(runner.shutdown(data, timeout))

    # Return whatever errors were discovered.
    errors = collect_errors_from(res)
    if errors:
        return StdRet.pass_error(errors)
    return RET_OK_NONE
