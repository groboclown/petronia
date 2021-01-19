"""Handles the chain of events for the loading process."""

from typing import List, Optional, Union
import uuid
from petronia_common.event_stream import (
    EventForwarderTarget, RawEvent,
    raw_event_id,
    as_raw_event_object_data, is_raw_event_object,
)
from petronia_common.extension.config import ImplExtensionMetadata, StandAloneExtensionMetadata
from petronia_common.util import (
    PetroniaReturnError, StdRet, UserMessage, join_errors,
)
from petronia_common.util import i18n as _
from petronia_extension_loader.context import EventHandlerContext
from .send import (
    EXTENSION_LOADER_FOREMAN_SOURCE,
    send_start_launcher_request,
    send_load_extension_failed,
    send_foreman_start_extension_request,
)
from .. import messages
from ..defs import Timeout, ExtensionInfo, TRANSLATION_CATALOG
from ..events.impl.extension_loader import EXTENSION_NAME as EXTENSION_LOADER_NAME
from ..events.impl.extension_loader import Error as ElError
from ..events.impl.extension_loader import Arguments as ElArguments
from ..events.impl.foreman import (
    StartLauncherSuccessEvent, StartLauncherFailedEvent,
    LauncherLoadExtensionRequestEvent,
    LauncherLoadExtensionSuccessEvent, LauncherLoadExtensionFailedEvent,
)
from ..events.impl.foreman import Error as ForemanError


LOAD_ERROR_SOURCE_ID = EXTENSION_LOADER_NAME + ':load-failure'
NO_SOURCE_TARGET_IDS = (EXTENSION_LOADER_NAME + ':load-extension',)


# Some notes:
#   Loading progress is recorded in the context LoadList.
#   When an extension has completed loading, also the function
#     boot_extension_handler.on_extension_load_complete
#   must be called.


START_LAUNCHER_RESPONSE_EVENT_IDS = (
    StartLauncherSuccessEvent.FULL_EVENT_NAME,
    StartLauncherFailedEvent.FULL_EVENT_NAME,
)
START_EXTENSION_RESPONSE_EVENT_IDS = (
    LauncherLoadExtensionSuccessEvent.FULL_EVENT_NAME,
    LauncherLoadExtensionFailedEvent.FULL_EVENT_NAME,
)


def start_extension_load_chain(
            context: EventHandlerContext,
            requesting_source_id: str,
            extension: ExtensionInfo,
            timeout: float,
) -> StdRet[None]:
    """Start the extension load chain of events and listeners.

    As a precondition, the extension must have already been loaded into the
    load_list.
    """
    metadata = extension.metadata
    if not isinstance(metadata, (ImplExtensionMetadata, StandAloneExtensionMetadata)):
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('Can only start a non-API extension; requested to start {name}'),
            name=extension.name,
        )
    extension.add_request_source_id(requesting_source_id)
    if not context.load_list().is_pending(extension.name):
        # This might have already
        return StdRet.pass_errmsg(
            TRANSLATION_CATALOG,
            _('Extension {name} is not pending.  Skipping extension load chain for this request.'),
            name=extension.name,
        )
    handler = StartLauncherResponseHandler(
        context, extension, metadata, timeout,
    )
    context.add_target(handler)
    res = send_start_launcher_request(
        context=context,
        identifier=handler.launcher_id,
        launcher=metadata.runtime.launcher,
        permissions=metadata.runtime.requested_permissions,
    )
    if res.has_error:
        return res
    context.load_list().mark_loading(extension.name)
    return res


class StartLauncherResponseHandler(EventForwarderTarget, Timeout):
    """
    Listens to the responses for starting a launcher.
    """

    __slots__ = (
        '_context', '_launcher_id', '_handler_id',
        '_metadata', '_extension',
    )

    def __init__(
            self,
            context: EventHandlerContext,
            extension_info: ExtensionInfo,
            extension_metadata: Union[ImplExtensionMetadata, StandAloneExtensionMetadata],
            timeout: float,
    ) -> None:
        assert extension_info.metadata == extension_metadata
        Timeout.__init__(self, timeout)
        self._context = context
        self._extension = extension_info
        self._metadata = extension_metadata
        self._launcher_id = create_launcher_handle()
        self._handler_id: Optional[str] = None

    @property
    def launcher_id(self) -> str:
        """Get the internal launcher ID."""
        return self._launcher_id

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        if event_id not in START_LAUNCHER_RESPONSE_EVENT_IDS:
            return False
        if target_id != EXTENSION_LOADER_FOREMAN_SOURCE:
            return False
        return True

    def on_error(self, error: PetroniaReturnError) -> bool:
        return self.is_timed_out()

    def on_eof(self) -> None:
        pass

    def consume(self, event: RawEvent) -> bool:
        # Consume the event.
        # If this doesn't handle the event but has timed out, then remove the listener.
        if not is_raw_event_object(event):
            return self.is_timed_out()
        ret = False
        event_id = raw_event_id(event)
        raw_object = as_raw_event_object_data(event)
        if event_id == StartLauncherSuccessEvent.FULL_EVENT_NAME:
            success_event_res = StartLauncherSuccessEvent.parse_data(raw_object)
            if success_event_res.has_error:
                # Ignore parse error.
                messages.display_message(
                    success_event_res, 'Failed to parse StartLauncherSuccessEvent',
                )
                return self.is_timed_out()
            ret = self._handle_success(success_event_res.result)
        elif event_id == StartLauncherFailedEvent.FULL_EVENT_NAME:
            failed_event_res = StartLauncherFailedEvent.parse_data(raw_object)
            if failed_event_res.has_error:
                # Ignore parse error.
                messages.display_message(
                    failed_event_res, 'Failed to parse StartLauncherFailedEvent',
                )
                return self.is_timed_out()
            ret = self._handle_failure(failed_event_res.result)

        # Event is not valid for this launcher; ignore
        if not ret:
            # Not handled, so only remove if this handler has timed out.
            return self.is_timed_out()
        return True

    def _handle_success(self, event: StartLauncherSuccessEvent) -> bool:
        """Handle a valid success message."""
        if event.identifier != self._launcher_id:
            # Not for this handler.
            return False

        # Set up the next handler in the chain.
        self._context.add_target(StartExtensionResponseHandler(
            self._context,
            self._extension,
            self._launcher_id,
            self.remaining_time(),
        ))

        # Tell the launcher to start loading the extension.
        send_foreman_start_extension_request(
            self._context,
            self._extension,
            self._context.load_list().get_loaded(),
        )

        # This handler is done, and we've pushed the next phase in the chain
        # to the next handler.  So, remove this one.
        return True

    def _handle_failure(self, event: StartLauncherFailedEvent) -> bool:
        """Handle a valid failure message."""
        if event.identifier != self._launcher_id:
            # Not for us
            return False
        # We failed to load.  Send out the failure, if we're still loading...
        if not self._context.load_list().is_loading(self._extension.name):
            # TODO this is a bad state.  Somehow report it.
            # Remove this listener from the event forwarder.
            return True
        res = on_load_failure(self._context, self._extension, event.error)
        if res.has_error:
            messages.display_message(res, f'failed to load extension {self._extension.name}')
        # Remove this listener from the event forwarder.
        return True


class StartExtensionResponseHandler(EventForwarderTarget, Timeout):
    """Handle the response from sending an extension start request to foreman."""

    __slots__ = ('_context', '_extension', '_launcher_id', '_extension',)

    def __init__(
            self,
            context: EventHandlerContext,
            extension: ExtensionInfo,
            launcher_id: str,
            timeout: float,
    ) -> None:
        self._context = context
        self._extension = extension
        self._launcher_id = launcher_id
        Timeout.__init__(self, timeout)

    def can_consume(self, event_id: str, source_id: str, target_id: str) -> bool:
        if event_id not in START_EXTENSION_RESPONSE_EVENT_IDS:
            return False
        if source_id != LauncherLoadExtensionRequestEvent.UNIQUE_TARGET_FQN:
            return False
        if target_id != self._launcher_id:
            return False
        return True

    def on_error(self, error: PetroniaReturnError) -> bool:
        return self.is_timed_out()

    def on_eof(self) -> None:
        pass

    def consume(self, event: RawEvent) -> bool:
        if not is_raw_event_object(event):
            return self.is_timed_out()
        event_id = raw_event_id(event)
        raw_event_obj = as_raw_event_object_data(event)
        res = False
        if event_id == LauncherLoadExtensionSuccessEvent.FULL_EVENT_NAME:
            success_event_res = LauncherLoadExtensionSuccessEvent.parse_data(raw_event_obj)
            if success_event_res.has_error:
                # Ignore parse error.
                messages.display_message(
                    success_event_res, 'Failed to parse LauncherLoadExtensionSuccessEvent',
                )
                return self.is_timed_out()
            res = self._handle_success(success_event_res.result)
        elif event_id == LauncherLoadExtensionFailedEvent.FULL_EVENT_NAME:
            failed_event_res = LauncherLoadExtensionFailedEvent.parse_data(raw_event_obj)
            if failed_event_res.has_error:
                # Ignore parse error.
                messages.display_message(
                    failed_event_res, 'Failed to parse LauncherLoadExtensionFailedEvent',
                )
                return self.is_timed_out()
            res = self._handle_failure(failed_event_res.result)

        if not res:
            return self.is_timed_out()
        return True

    def _handle_success(self, event: LauncherLoadExtensionSuccessEvent) -> bool:
        raise NotImplementedError

    def _handle_failure(self, event: LauncherLoadExtensionFailedEvent) -> bool:
        """Handle a valid failure message."""
        # We failed to load.  Send out the failure, if we're still loading...
        if not self._context.load_list().is_loading(self._extension.name):
            # TODO this is a bad state.  Somehow report it.
            # Remove this listener from the event forwarder.
            return True
        res = on_load_failure(self._context, self._extension, event.error)
        if res.has_error:
            messages.display_message(res, f'failed to load extension {self._extension.name}')
        # Remove this listener from the event forwarder.
        return True


def on_load_failure(
        context: EventHandlerContext,
        extension: ExtensionInfo,
        error: ForemanError,
) -> StdRet[None]:
    """Failed to load the extension for some reason.  This requires pushing
    out failure events for this and any dependent extensions."""
    load_list = context.load_list()
    failed_reaction_res = load_list.mark_failed(extension.name)
    if failed_reaction_res.has_error:
        return failed_reaction_res.forward()
    el_error = ElError(error.identifier, error.source, error.message, [
        ElArguments(arg.name, arg.value)
        for arg in error.arguments
    ])
    errors = send_load_extension_failed_to_all(context, extension, el_error)
    to_fail = list(failed_reaction_res.result)
    while to_fail:
        ext = to_fail.pop()
        if not ext or not load_list.is_pending(ext.name):
            continue
        new_failed_res = load_list.mark_failed(ext.name)
        if new_failed_res.has_error:
            errors.extend(new_failed_res.error_messages())
        else:
            errors.extend(send_load_extension_failed_to_all(context, ext, el_error))
            to_fail.extend(new_failed_res.result)
    return StdRet.pass_error(join_errors(*errors))


def send_load_extension_failed_to_all(
        context: EventHandlerContext,
        extension: ExtensionInfo,
        error: ElError,
) -> List[UserMessage]:
    """Send a load extension failed event to all origin sources."""
    errors: List[UserMessage] = []
    for request_source_id in extension.request_source_ids or NO_SOURCE_TARGET_IDS:
        res = send_load_extension_failed(
            context=context,
            request_source_id=request_source_id,
            extension_name=extension.name,
            error=error,
        )
        errors.extend(res.error_messages())
    return errors


def create_launcher_handle() -> str:
    """Create a unique handle."""
    return EXTENSION_LOADER_NAME + ':loader-' + str(uuid.uuid4())
