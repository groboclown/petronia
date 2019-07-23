
"""
An in-memory handler for verifying that data came from a trusted source.
This supports both a signature and encryption.

This uses a public/private key pair.  The client maintains a list of trusted
public keys.  The trusted senders include an envelope, encrypted with the
private key.  The envelope includes a hash of the message and a message index.
The client needs to maintain a minimal key number along with a recent cache
of seen indicies (this allows for a constant memory size).

Due to the time involved in creating one of these messages, they need to be
limited to critical actions.
"""


def is_memory_crypto_available() -> bool:
    """
    Is the underlying implementation for the memory cryptography API available
    for use?  If False, then those methods will raise an error on use.
    """
    return False

#from typing import Tuple, Dict
#def create_trust_envelope(
#        sender: str,
#        private_key: bytes,
#        message_index: int,
#        event_obj: object
#) -> bytes:
#    """
#    Creates the signed byte string of the envelope.
#    This should be added as the `signature` value of the event object.
#    """
#    # This will just create a signed byte string.
#    # The
#    pass
#
#TrustedSenders = Dict[str, Tuple[bytes, int]]
#
#def verify_trust_envelope(
#    trusted_senders: TrustedSenders,
#    event_obj: object
#) -> Tuple[bool, int]:
#    """
#    Checks the event_obj `signature` value against the store of
#    trusted senders.
#    """
#    pass
