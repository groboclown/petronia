
"""
Basic disposer class and support.
"""

from ...util import RWLock
from ...errors import assert_state

def is_disposable(obj):
    """Checks if the object argument can be used by the dispose."""
    return hasattr(obj, 'dispose') and callable(obj.dispose)


class Disposer:
    """
    Handles parent/child relationships and proper disposal.

    :param error_handler callable: a function that is invoked when a dispose invocation
        raises an exception.
    """
    def __init__(self, error_handler: callable):
        assert callable(error_handler)
        self.__disp = {}
        self.__lock = RWLock()
        self.__error_handler = error_handler

    def register(self, target_id: str, obj: object, parent_id: str or None):
        """
        Register an object for disposing.  Can only be done once per target_id, until
        it has been disposed.

        `dispose` methods should be idempotent - meaning that it is written in such a way
        that calling it multiple times isn't harmful.
        """
        assert isinstance(target_id, str)
        assert target_id
        assert parent_id is None or (isinstance(parent_id, str) and parent_id)
        assert is_disposable(obj)

        self.__lock.acquire_write()
        try:
            if target_id in self.__disp:
                # Could have been registered as a parent before it itself was registered,
                # which is fine.  We need to preserve the dependency list.
                assert_state(
                    self.__disp[target_id][0] is None,
                    'Disposer',
                    'Can only register target object {0} once without disposing it'.format(target_id)
                )
                self.__disp[target_id][0] = obj
            else:
                self.__disp[target_id] = [obj, parent_id, []]
            if parent_id:
                if parent_id in self.__disp:
                    self.__disp[parent_id][1].append(target_id)
                else:
                    self.__disp[parent_id] = [None, [target_id]]
        finally:
            self.__lock.release()

    def dispose(self, target_id: str):
        """
        Dispose the given target_id and all its registered children.
        Does not fail if the target is not registered.

        Returns a list of all the target_ids that were disposed by this
        action.
        """
        disposed_ids = []
        self.__lock.acquire_write()
        stack = [[target_id, 0, None]]
        try:
            while stack:
                next_id, action, dispose_obj = stack.pop()
                if action == 0:
                    # Descending into the children.
                    # The dispose_obj is not set to anything meaningful
                    # at this point.
                    if next_id in self.__disp:
                        dispose_obj, child_ids = self.__disp[next_id]
                        # Note the immediate removal of the dispose registration.
                        # This prevents infinite loops.
                        del self.__disp[next_id]
                        for cid in child_ids:
                            stack.append([cid, 0, None])
                        stack.append([next_id, 1, dispose_obj])
                elif action == 1:
                    # All the children have been handled.
                    try:
                        dispose_obj.dispose()
                    except BaseException as err: # pylint: disable=broad-except
                        self.__error_handler(next_id, dispose_obj, err)
                    disposed_ids.append(next_id)
                # else it's a bad programming state.  But because this
                # method is so short, we won't check this state.
        finally:
            self.__lock.release()
        return disposed_ids
