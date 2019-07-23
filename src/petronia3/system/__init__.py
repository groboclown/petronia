
"""
Parts of Petronia that tie everything together.

These are the core systems that allow directly interaction by participants.

Note that items that insert themselves into an environment under the system
module do not include the ability to remove themselves; they are expected to
always be active.
"""

from . import bus, events, logging, participant
