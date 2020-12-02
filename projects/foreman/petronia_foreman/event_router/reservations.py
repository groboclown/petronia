"""
Allows for the route controller to manage per-channel event targets.

ChannelReservationCallback - a callback registered with the ChannelReservations
that takes the channel name as the first argument, and returns either an error
(such as the channel can't be reserved), or an optional event target.  This
callback can be stateful, to allow for handling scenarios where at most only
one channel with a name can be reserved, or only one event listener can be
used.
"""

from typing import List, Tuple, Set, Callable, Optional, Union
import re
from petronia_common.event_stream import EventForwarderTarget
from petronia_common.util import StdRet, RET_OK_NONE
from petronia_common.util import i18n as _
from ..constants import TRANSLATION_CATALOG


# Called when the channel attempts to be reserved.  For channels that
# have at most 1 registration, this will return an error.  This is stateful,
# which allows the first registration to be okay, and subsequent to fail.
#
# If the reservation requires an event target, then that is returned.
ChannelReservationCallback = Callable[[str], StdRet[Optional[EventForwarderTarget]]]


class ChannelReservations:
    """Manages event listeners that are assigned to specific channel names,
    and can prevent some channel names from being registered.

    Any channel registration request that does not have a corresponding matcher
    is considered to be okay to reserve.  The matchers are registered in-order, and
    checked in reverse order.  To prevent all but a small number of channel names,
    register a '.*' pattern as the first item.

    This is thread-unsafe.  Locking must be done by the caller."""
    __slots__ = ('__channel_callbacks', '__reserved',)

    def __init__(self) -> None:
        self.__channel_callbacks: List[Tuple[re.Pattern, ChannelReservationCallback]] = []
        self.__reserved: Set[str] = set()

    def add_channel_reservation_callback(
            self,
            channel: Union[str, re.Pattern],
            callback: ChannelReservationCallback,
    ) -> StdRet[None]:
        """Add a channel pattern reservation."""
        channel_re: re.Pattern
        if isinstance(channel, str):
            channel_re = re.compile('^' + re.escape(channel) + '$')
        else:
            channel_re = channel
        for key, _callback in self.__channel_callbacks:
            if key.pattern == channel_re.pattern:
                return StdRet.pass_errmsg(
                    TRANSLATION_CATALOG,
                    _('attempted to add duplicate channel pattern ({pattern})'),
                    pattern=repr(channel),
                )
        # Add this to the start of the reservation list, so that the first registered are
        # checked last.
        self.__channel_callbacks.insert(0, (channel_re, callback))
        return RET_OK_NONE

    def reserve_channel(self, name: str) -> StdRet[Optional[EventForwarderTarget]]:
        """Attempt to reserve the channel name.  If it can be reserved, then the target is
        returned (if any).  Otherwise, an error is returned."""
        # First, check if the name is currently reserved.
        if name in self.__reserved:
            return StdRet.pass_errmsg(
                TRANSLATION_CATALOG,
                _('channel name already reserved ({name})'),
                channel=name,
            )
        for key, callback in self.__channel_callbacks:
            if key.match(name):
                res = callback(name)
                if res.ok:
                    self.__reserved.add(name)
                return res
        self.__reserved.add(name)
        return RET_OK_NONE

    def release_channel(self, name: str) -> bool:
        """Releases the reservation on a channel name.  Returns True if it was released, or False
        if it was not reserved."""
        try:
            self.__reserved.remove(name)
            return True
        except KeyError:
            return False
