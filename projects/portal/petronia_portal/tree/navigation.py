"""Functionality to navigate through the tree model."""

from typing import List, Tuple, Optional
from . import model

WRAP_MODE__NONE = 'none'
WRAP_MODE__SCREEN = 'wrap-screen'
WRAP_MODE__BLOCK = 'wrap-block'


# A valid tile path must terminate in a Portal.
# The path is in reverse order, meaning the portal is the first element, and the
# start of the tree is the last element.  The path element entry is the child index, tile
# at that index.
TilePathElement = Tuple[int, model.Tile]
TilePath = List[TilePathElement]


def get_path_for_portal_alias(parent: model.TileIterator, portal_alias: str) -> TilePath:
    """Find the child index within the splits to the portal with the given alias.  The parent
    argument is not added to the path.  The returned path is only valid until the layout changes.
    A zero-length return value means that the portal was not found.

    Currently, this is slow and painful."""
    children = parent.get_children()
    for index in range(len(children)):  # pylint:disable=consider-using-enumerate
        child = children[index]
        if isinstance(child, model.Portal) and child.has_portal_alias(portal_alias):
            return [(index, child)]
        if isinstance(child, model.TileContainer):
            child_path = get_path_for_portal_alias(child, portal_alias)
            if child_path:
                child_path.append((index, child))
                return child_path
            # else the alias is not in the child.
    # Cannot return the static EMPTY_LIST, because it might be used.
    return []


def get_path_for_portal_id(parent: model.TileIterator, portal_id: int) -> TilePath:
    """Find the child index within the splits to the portal with the given alias.  The parent
    argument is not added to the path.  The returned path is only valid until the layout changes.
    A zero-length return value means that the portal was not found.

    Currently, this is slow and painful."""
    children = parent.get_children()
    for index in range(len(children)):  # pylint:disable=consider-using-enumerate
        child = children[index]
        if isinstance(child, model.Portal) and child.portal_id == portal_id:
            return [(index, child)]
        if isinstance(child, model.TileContainer):
            child_path = get_path_for_portal_id(child, portal_id)
            if child_path:
                child_path.append((index, child))
                return child_path
            # else the alias is not in the child.
    # Cannot return the static EMPTY_LIST, because it might be used.
    return []


def contained_portals(parent: model.Tile) -> List[model.Portal]:
    """Return all the portals under the parent."""
    if isinstance(parent, model.Portal):
        return [parent]
    ret: List[model.Portal] = []
    if isinstance(parent, model.TileContainer):
        for child in parent.get_children():
            ret.extend(contained_portals(child))
    return ret


def portals_in_block(root: model.TileIterator, active: TilePath) -> List[model.Portal]:
    """Return all the portals within the screen block of the active path."""
    # Look up the active path until we get to a block split.
    # Don't need to look at index 0, because that should be a portal.
    block_index = 1
    while block_index < len(active):
        item = active[block_index][1]
        if isinstance(item, model.TileContainer) and item.covers_screen_block:
            return contained_portals(item)
    # No block defined, so just use the root.
    return contained_portals(root)


def first_portal(root: model.Tile) -> TilePath:
    """By definition, a split should terminate in a Portal, but it might not."""
    path: List[TilePathElement] = []
    # Note that the root is never inserted into the path.
    parent = root
    while isinstance(parent, model.TileContainer):
        assert isinstance(parent, model.TileContainer)  # nosec  # mypy and others kind of want this
        children = parent.get_children()
        if len(children) <= 0:
            # invalid setup.
            return []
        parent = children[0]
        path.insert(0, (0, parent))
    return path


def last_portal(root: model.Tile) -> TilePath:
    """By definition, a split should terminate in a Portal, but it might not."""
    path: List[TilePathElement] = []
    # Note that the root is never inserted into the path.
    parent = root
    while isinstance(parent, model.TileContainer):
        assert isinstance(parent, model.TileContainer)  # nosec  # mypy and others kind of want this
        children = parent.get_children()
        if len(children) <= 0:
            # invalid setup.
            return []
        index = len(children) - 1
        parent = children[index]
        path.insert(0, (index, parent))
    return path


def get_parent_split(
        root: model.TileIterator, path: TilePath, path_index: int,
) -> Optional[model.TileIterator]:
    """Find the parent split of the path at the given index."""
    parent_index = path_index + 1
    if parent_index >= len(path):
        return root
    ret = path[path_index][1]
    if isinstance(ret, model.TileContainer):
        return ret
    # Bad state
    return None


def navigate_previous(root: model.TileIterator, active: TilePath, wrap: str) -> TilePath:
    """Navigate from the active portal to the previous portal.  The active path must have the
    root as its parent."""
    if not active:
        # Just use the last portal.
        return last_portal(root)

    # Find the portal in the parent's previous.
    path_index = 0
    while path_index < len(active) - 1:
        parent = active[path_index + 1][1]
        if not isinstance(parent, model.TileContainer):
            # Invalid setup.
            return []
        if active[path_index][0] > 0:
            child_index = active[path_index][0] - 1
            child = parent.get_children()[child_index]
            sub_path = last_portal(child)
            return [*sub_path, (child_index, child), *active[path_index + 1:]]

        # Otherwise, the parent's parent needs to be looked at.
        if parent.covers_screen_block and wrap == WRAP_MODE__BLOCK:
            # reached the end of the screen block, so wrap around to the
            # end of the block.
            return [*last_portal(parent), *active[path_index + 1:]]
        path_index += 1

    # The last item in the path is relative to the root.

    if wrap == WRAP_MODE__NONE:
        # No wrapping, so return the first portal.
        return first_portal(root)

    # Wrapping the whole screen, so return the very last portal.
    return last_portal(root)


def navigate_next(root: model.TileIterator, active: TilePath, wrap: str) -> TilePath:
    """Navigate from the active portal to the given direction.  The active path must have the
    root as its parent."""
    if not active:
        # Just use the first portal.
        return first_portal(root)

    path_index = 0
    while path_index < len(active) - 1:
        parent = active[path_index + 1][1]
        if not isinstance(parent, model.TileContainer):
            # Invalid setup
            return []
        children = parent.get_children()
        last_child_index = len(children) - 1
        if active[path_index][0] < last_child_index:
            child_index = active[path_index][0] + 1
            child = children[child_index]
            sub_path = last_portal(child)
            return [*sub_path, (child_index, child), *active[path_index + 1:]]

        # Otherwise, the parent's parent needs to be looked at.
        if parent.covers_screen_block and wrap == WRAP_MODE__BLOCK:
            # reached the end of the screen block, so wrap around to the
            # start of the block.
            return [*first_portal(parent), *active[path_index + 1:]]

        path_index += 1

    # The last item in the path is relative to the root.

    if wrap == WRAP_MODE__NONE:
        # No wrapping, so return the last portal.
        return last_portal(root)

    # Wrapping the whole screen, so return the very first portal.
    return first_portal(root)


def navigate_up(root: model.TileIterator, active: TilePath, wrap: str) -> Optional[model.Portal]:
    """Navigate from the active portal to the given direction.  The active path must have the
    root as its parent."""
    if not active:
        return None

    # Keep the position of the moved-to portal within the x-y bounds of the active portal.
    min_x = active[0][1].pos_x
    max_x = min_x + active[0][1].width
    above_y = active[0][1].pos_y

    # This gets all the portals and finds the best match within the x-y range.
    if wrap == WRAP_MODE__BLOCK:
        all_portals = portals_in_block(root, active)
    else:
        all_portals = contained_portals(root)

    best_y = -10000000000
    best_match: Optional[model.Portal] = None
    for portal in all_portals:
        portal_max_y = portal.pos_y + portal.height
        if (
            above_y >= portal_max_y > best_y
            and portal.pos_x < max_x
            and portal.pos_x + portal.width >= min_x
        ):
            best_match = portal
            best_y = portal_max_y

    if best_match:
        return best_match

    # TODO wrap-around if in screen wrap mode
    return None


def navigate_down(root: model.TileIterator, active: TilePath, wrap: str) -> Optional[model.Portal]:
    """Navigate from the active portal to the given direction.  The active path must have the
    root as its parent."""
    if len(active) == 0:
        return None

    # Keep the position of the moved-to portal within the x-y bounds of the active portal.
    min_x = active[0][1].pos_x
    max_x = min_x + active[0][1].width
    below_y = active[0][1].pos_y + active[0][1].height

    # This gets all the portals and finds the best match within the x-y range.
    if wrap == WRAP_MODE__BLOCK:
        all_portals = portals_in_block(root, active)
    else:
        all_portals = contained_portals(root)

    best_y = 100000000
    best_match: Optional[model.Portal] = None
    for portal in all_portals:
        if (
            best_y > portal.pos_y >= below_y
            and portal.pos_x < max_x
            and portal.pos_x + portal.width >= min_x
        ):
            best_match = portal
            best_y = portal.pos_y

    # TODO wrap-around if in screen wrap mode
    return best_match


def navigate_left(root: model.TileIterator, active: TilePath, wrap: str) -> Optional[model.Portal]:
    """Navigate from the active portal to the given direction.  The active path must have the
    root as its parent."""
    if not active:
        return None

    # Keep the position of the moved-to portal within the x-y bounds of the active portal.
    min_y = active[0][1].pos_y
    max_y = min_y + active[0][1].height
    above_x = active[0][1].pos_x

    # This gets all the portals and finds the best match within the x-y range.
    if wrap == WRAP_MODE__BLOCK:
        all_portals = portals_in_block(root, active)
    else:
        all_portals = contained_portals(root)

    best_x = -10000000000
    best_match: Optional[model.Portal] = None
    for portal in all_portals:
        portal_max_x = portal.pos_x + portal.width
        if (
            above_x >= portal_max_x > best_x
            and portal.pos_y < max_y
            and portal.pos_y + portal.height >= min_y
        ):
            best_match = portal
            best_x = portal_max_x

    # TODO wrap-around if in screen wrap mode
    return best_match


def navigate_right(root: model.TileIterator, active: TilePath, wrap: str) -> Optional[model.Portal]:
    """Navigate from the active portal to the given direction.  The active path must have the
    root as its parent."""
    if not active:
        # Just use the first portal.
        return None

    # Keep the position of the moved-to portal within the x-y bounds of the active portal.
    min_y = active[0][1].pos_y
    max_y = min_y + active[0][1].height
    below_x = active[0][1].pos_x + active[0][1].width

    # This gets all the portals and finds the best match within the x-y range.
    if wrap == WRAP_MODE__BLOCK:
        all_portals = portals_in_block(root, active)
    else:
        all_portals = contained_portals(root)

    best_x = 100000000
    best_match: Optional[model.Portal] = None
    for portal in all_portals:
        if (
            best_x > portal.pos_x >= below_x
            and portal.pos_y < max_y
            and portal.pos_y + portal.height >= min_y
        ):
            best_match = portal
            best_x = portal.pos_x

    # TODO wrap-around if in screen wrap mode
    return best_match
