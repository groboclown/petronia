
"""
Basic disposer class and support.
"""

from typing import Dict, List, Tuple, Optional


class Disposer:
    """
    Handles parent/child relationships and sending disposal signals.  It does not
    maintain any references to the objects being disposed.
    """

    __disp: Dict[str, List[str]]

    def __init__(self) -> None:
        self.__disp = dict()

    def register(self, target_id: str, parent_id: Optional[str] = None) -> None:
        """
        Register an object for disposing.  Can only be done once per target_id, until
        it has been disposed.

        `dispose` methods should be idempotent - meaning that it is written in such a way
        that calling it multiple times isn't harmful.
        """
        assert isinstance(target_id, str)
        assert target_id
        assert parent_id is None or (isinstance(parent_id, str) and parent_id)

        if target_id not in self.__disp:
            # Could have been registered as a parent before it itself was registered,
            # which is fine.  We need to preserve the dependency list.
            self.__disp[target_id] = []
        if parent_id:
            if parent_id in self.__disp:
                self.__disp[parent_id].append(target_id)
            else:
                self.__disp[parent_id] = [target_id]

    def dispose(self, target_id: str) -> List[str]:
        """
        Dispose the given target_id and all its registered children.
        Does not fail if the target is not registered.

        Returns a list of all the target_ids that were disposed by this
        action, in the order that the disposal must happen.

        Note that, because the disposer does not maintain the objects to
        dispose, no disposal happened on those objects, but the internal
        maintenance of the dependency tree has been disposed.
        """
        disposed_ids: List[str] = []
        stack: List[Tuple[str, int]] = [(target_id, 0)]
        while stack:
            next_id, action = stack.pop()
            if action == 0:
                # Descending into the children.
                # The dispose_obj is not set to anything meaningful
                # at this point.
                if next_id in self.__disp:
                    child_ids: List[str] = self.__disp[next_id]
                    # Note the immediate removal of the dispose registration.
                    # This prevents infinite loops.
                    del self.__disp[next_id]
                    for cid in child_ids:
                        stack.append((cid, 0))
                    stack.append((next_id, 1))
            elif action == 1:
                # All the children have been handled.
                disposed_ids.append(next_id)
            # else it's a bad programming state.  But because this
            # method is so short, we won't check this state.
        return disposed_ids
