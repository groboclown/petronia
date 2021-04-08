"""Generates handler IDs.

This is incredibly important to have consistency; without it, stuff won't be connecting
correctly."""


def create_handler_id(extension_name: str) -> str:
    """Create a unique handler ID for the extension."""
    if extension_name.startswith('handler-id::'):
        print(
            f"************ ERROR: something is using handler-id instead of "
            f"extension_name ({extension_name}"
        )
        return extension_name
    return 'handler-id::' + extension_name
