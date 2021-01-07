"""Event streaming entrypoint."""

from petronia_common.event_stream import BinaryReader, BinaryWriter
from .event_router import create_router


def entrypoint(inp: BinaryReader, outp: BinaryWriter) -> None:
    """Standardized entrypoint for event stream handling.
    Can be used for the in-memory launcher."""
    router = create_router(inp, outp)
    router.handle_source()
