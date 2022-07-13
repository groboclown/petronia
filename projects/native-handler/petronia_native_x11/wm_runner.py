"""The phase runner for the window manager."""

from petronia_common.util import StdRet, RET_OK_NONE
from petronia_ext_lib.runner import EventRegistryContext
from petronia_native.common import user_messages
from . import hook_types, common_data, running_data
from .configuration import ConfigurationStore
from .event_handler import EventHandlerLoop
from .wm_connect import connect_as_wm


class WindowManagerPhaseRunner(hook_types.PhaseRunner):
    """The phase runner."""

    def boot(
            self, context: EventRegistryContext, config: ConfigurationStore,
    ) -> StdRet[common_data.Libraries]:
        return common_data.Libraries.create(
            context=context,
            config=config,
            warning_report=lambda x: user_messages.low_println(x.debug()),
        )

    def become_window_manager(
            self, libs: common_data.Libraries,
    ) -> StdRet[common_data.WindowManagerData]:
        return connect_as_wm(libs)

    def prepare_event_loop(
            self, data: common_data.WindowManagerData,
    ) -> StdRet[running_data.RunningData]:
        data.libs.xcb.xcb_ungrab_server(data.connection)

        event_loop = EventHandlerLoop(
            cxt=data,

            # TODO replace with a real handler
            on_error=lambda x: user_messages.low_traceback(x),

            # TODO allow configuring queue wait time?
        )
        # event_loop.add_missed_events(cxt.pending_events)

        return StdRet.pass_ok(running_data.RunningData(
            wm_data=data,
            event_loop=event_loop,
        ))

    def run_event_loop(self, data: running_data.RunningData) -> StdRet[None]:
        data.event_loop.start()
        return RET_OK_NONE

    def shutdown(self, data: running_data.RunningData, timeout: float) -> StdRet[None]:
        # TODO do some nice extra shutdown
        data.xcb.xcb_disconnect(data.connection)
        return RET_OK_NONE