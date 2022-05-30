"""The phase runner for the window manager."""

from petronia_common.util import StdRet, RET_OK_NONE
from petronia_ext_lib.runner import LookupEventRegistryContext
from petronia_native.common import user_messages
from . import hook_types, common_data, event_handler
from .configuration import ConfigurationStore
from .event_handler import EventHandlerLoop
from .wm_connect import connect_as_wm


class WindowManagerPhaseRunner(hook_types.PhaseRunner):
    """The phase runner."""

    def boot(
            self, context: LookupEventRegistryContext, config: ConfigurationStore,
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
    ) -> StdRet[common_data.CommonData]:
        no_res = event_handler.setup_event_listener_with_screen(data)
        if no_res.has_error:
            data.libs.xcb.xcb_disconnect(data.connection)
            return no_res.forward()

        data.libs.xcb.xcb_ungrab_server(data.connection)

        ret = common_data.CommonData(
            wm_data=data,
        )

        event_loop = EventHandlerLoop(
            cxt=ret,

            # TODO replace with a real handler
            on_error=lambda x: user_messages.low_traceback(x),

            # TODO allow configuring queue wait time?
        )
        event_loop.add_missed_events(cxt.pending_events)
        ret = WMRet(xcb_api, event_loop)

    def run_event_loop(self, data: common_data.CommonData) -> StdRet[None]:
        pass

    def shutdown(self, data: common_data.CommonData, timeout: float) -> StdRet[None]:
        # TODO do some nice extra shutdown
        data.xcb.xcb_disconnect(data.connection)
        return RET_OK_NONE
