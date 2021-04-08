
"""
Requests to perform an action.
"""


class LaunchPetroniaProcess:
    """
    Launch a Petronia-aware process.  The process will be tied through a private
    connection to the event bus.  Could be extra FD, could be a private pipe.
    """
