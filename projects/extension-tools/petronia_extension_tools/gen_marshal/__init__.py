
"""Generate the marshalling functions and classes for an extension's events.

To run this tool:

$ PYTHONPATH=projects/extension-tools:projects/py-common-lib python3 -m \
    python3 -m petronia_extension_tools.gen_marshal \
    --out (sourcecode output directory) \
    (list of extension yaml files)

Optionally, these arguments can also be given:
    --language (language name)
    Generate for a different language.  Currently, only Python is supported.

    --implementation
    Generate internal events for implementations.  Otherwise, just events that
    are sent or received publicly (or just for the target) are allowed.
"""
