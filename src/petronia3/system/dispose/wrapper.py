
"""
Wrappers for creating new disposers.
"""

class CallableDisposer:
    """
    Converts a function call into a dispose method.
    """
    def __init__(self, fcn: callable):
        assert callable(fcn)
        self.__call = fcn

    def dispose(self):
        """Idempotent dispose call."""
        if self.__call:
            try:
                self.__call()
            finally:
                self.__call = None


class CloseableDisposer:
    """
    Converts an object with a "close" call into a dispose method.
    """
    def __init__(self, obj: object):
        assert hasattr(obj, 'close')
        assert callable(obj.close)
        self.__obj = obj

    def dispose(self):
        """Idempotent dispose call."""
        if self.__obj:
            try:
                self.__obj.close()
            finally:
                self.__obj = None
