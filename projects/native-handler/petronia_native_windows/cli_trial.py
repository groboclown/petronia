"""Test out the Windows native handler in a stand-alone applicaiton."""

from typing import Tuple, Sequence, List, Optional
import time

# This is supposed to be runnable as a CLI, so this needs absolute imports.
from petronia_native_windows import hook_messages, pumper, keymap
from petronia_native_windows.arch.native_funcs.monitor import are_monitors_different, WindowsMonitor
from petronia_native_windows.arch.native_funcs import WINDOWS_FUNCTIONS, HWND, WPARAM
from petronia_native.common import log

LAST_MONITOR_STATE: List[WindowsMonitor] = []


def key_callback(
        vk_code: int, scan_code: int, is_key_up: bool, _is_injected: bool,
) -> Tuple[bool, Sequence[Tuple[int, bool]]]:
    """on key press"""
    names = keymap.vk_to_names(vk_code)
    if is_key_up:
        log.low_print('Key Released: {vk} / {scan} / {names}'.format(
            vk=vk_code, scan=scan_code, names=names,
        ))
    else:
        log.low_print('Key Pressed: {vk} / {scan} / {names}'.format(
            vk=vk_code, scan=scan_code, names=names,
        ))

    return False, []


def check_monitor_state() -> None:
    """For anything that may cause the monitor state to change."""
    if callable(WINDOWS_FUNCTIONS.monitor.find_monitors):
        updated_monitors = WINDOWS_FUNCTIONS.monitor.find_monitors()  # pylint:disable=not-callable
        if are_monitors_different(LAST_MONITOR_STATE, updated_monitors):
            new_m = [m.info.export_data() for m in updated_monitors]
            log.low_print('Monitors changed: now {m}'.format(m=new_m))
            LAST_MONITOR_STATE.clear()
            LAST_MONITOR_STATE.extend(updated_monitors)


def display_changed() -> None:
    """display changed event callback."""
    check_monitor_state()


def system_changed(what: WPARAM) -> None:
    """system changed event callback."""
    log.low_print(f'System changed: 0x{what:04x}')
    check_monitor_state()


def device_changed(what: WPARAM) -> None:
    """device changed event callback."""
    log.low_print(f'Device changed: 0x{what:04x}')
    check_monitor_state()


def window_created(hwnd: HWND) -> None:
    """window created callback."""
    log.low_print(f'Window Created: {hwnd:08x}')


def window_destroyed(hwnd: HWND) -> None:
    """window destroyed callback."""
    log.low_print(f'Window Destroyed: {hwnd:08x}')


def window_focused(hwnd: HWND) -> Optional[bool]:  # pylint:disable=useless-return
    """window focused callback."""
    log.low_print(f'Window Focused: {hwnd:08x}')
    return None


def window_activated(hwnd: HWND) -> Optional[bool]:  # pylint:disable=useless-return
    """window activated callback."""
    log.low_print(f'Window Activated: {hwnd:08x}')
    return None


def window_activated_rude(hwnd: HWND) -> Optional[bool]:  # pylint:disable=useless-return
    """window activated rude callback."""
    log.low_print(f'Window Activated (Rudely!): {hwnd:08x}')
    return None


def redraw(hwnd: HWND) -> None:
    """redraw callback."""
    log.low_print(f'Redraw request for {hwnd:08x}')


def forced_exit(hwnd: HWND) -> Optional[bool]:  # pylint:disable=useless-return
    """forced exit callback."""
    log.low_print(f'Forced exit: {hwnd:08x}')
    return None


def window_changed_monitors(hwnd: HWND) -> None:
    """window changed monitors callback."""
    log.low_print(f'Window changed monitors: {hwnd:08x}')


def window_flashing(hwnd: HWND) -> None:
    """window flashing callback."""
    log.low_print(f'Window flashing: {hwnd:08x}')


def window_replacing(hwnd: HWND, with_hwnd: HWND) -> None:
    """window start replace callback."""
    log.low_print(f'Window replace start: {hwnd:08x} -> {with_hwnd:08x}')


def window_replaced(hwnd: HWND, with_hwnd: HWND) -> None:
    """window end replace callback."""
    log.low_print(f'Window replace end: {hwnd:08x} -> {with_hwnd:08x}')


def power_state_changed(suspending: bool) -> None:
    """power state changed callback."""
    log.low_print(f'Power state changed (suspended? {suspending}')


def taskman(hwnd: HWND, wparam: WPARAM) -> None:
    """task manager callback; don't expect it to work."""
    log.low_print(f'taskman message: {hwnd:08x} :: 0x{wparam:08x}')


def on_exit() -> None:
    """on message loop exit callback."""
    log.low_print('Exit message encountered.')


if __name__ == '__main__':
    if callable(WINDOWS_FUNCTIONS.monitor.find_monitors):
        LAST_MONITOR_STATE.clear()
        LAST_MONITOR_STATE.extend(WINDOWS_FUNCTIONS.monitor.find_monitors())  # pylint:disable=not-callable

    log.low_print(f'Initial monitors: {[m.info.export_data() for m in LAST_MONITOR_STATE]}')
    handler = pumper.WindowsHookPumper()
    handler.set_key_handler(key_callback)
    handler.add_message_handler(hook_messages.display_changed_message(display_changed))
    handler.add_message_handler(hook_messages.system_settings_changed_message(system_changed))
    handler.add_message_handler(hook_messages.device_changed_message(device_changed))
    handler.add_message_handler(hook_messages.window_created_message(window_created))
    handler.add_message_handler(hook_messages.window_destroyed_message(window_destroyed))
    handler.add_message_handler(hook_messages.shell_window_focused_message(window_focused))
    handler.add_message_handler(hook_messages.window_activated_message(window_activated))
    handler.add_message_handler(hook_messages.window_rude_activated_message(window_activated_rude))
    handler.add_message_handler(hook_messages.redraw_message(redraw))
    handler.add_message_handler(hook_messages.forced_exit_message(forced_exit))
    handler.add_message_handler(hook_messages.window_monitor_changed_message(
        window_changed_monitors,
    ))
    handler.add_message_handler(hook_messages.window_flash_message(window_flashing))
    handler.add_message_handler(hook_messages.window_replacing_message(window_replacing))
    handler.add_message_handler(hook_messages.window_replaced_message(window_replaced))
    handler.add_message_handler(hook_messages.system_power_state_changed(power_state_changed))
    handler.add_message_handler(hook_messages.taskman_message(taskman))
    handler.start(on_exit)

    log.low_print("Press ctrl-c to stop.")
    while True:
        time.sleep(500)
