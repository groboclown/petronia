
from ....aid.simp import (
    EventBus,
    EventId,
    ParticipantId,
)

from ...shutdown.api import (
    send_system_shutdown_request,
)


def on_shutdown_request(
        bus: EventBus
) -> None:
    send_system_shutdown_request(bus)

