"""
Launches extensions in-memory, rather than in another process.  Should mostly be used for testing.

Extensions compatible with this launcher MUST:

* provide a Python module with a name matching the extension name.
* provide a function in the module named 'extension_entrypoint' which takes the
    arguments (BinaryReader, BinaryWriter, Dict[str, Any], List[str]) and returns when
    the extension completes.
    The arguments are the event stream in / out, the loaded
    extension configuration, and the list of CLI arguments defined by
    the runtime configuration.

"""

from .memory_launcher import create_memory_launcher
