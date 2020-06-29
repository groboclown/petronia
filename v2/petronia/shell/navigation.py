
PORTAL_TYPE = 'portal'
LAYOUT_TYPE = 'layout'
DESTINATION_TYPES = (PORTAL_TYPE, LAYOUT_TYPE)

DIR_PARENT = 'parent'
DIR_NORTH = 'north'
DIR_SOUTH = 'south'
DIR_EAST = 'east'
DIR_WEST = 'west'
DIR_LEFT = DIR_WEST
DIR_RIGHT = DIR_EAST
DIR_UP = DIR_NORTH
DIR_DOWN = DIR_SOUTH
DIR_NEXT = 'next'
DIR_PREVIOUS = 'previous'

DIRECTIONS = (
    DIR_PARENT,
    DIR_NORTH, DIR_EAST, DIR_SOUTH, DIR_WEST,
    DIR_NEXT, DIR_PREVIOUS,
)
ROTATABLE_DIRECTIONS = (
    DIR_NEXT, DIR_PREVIOUS,
)


def create_direction_negotiation_start_event_obj(
        source_cid,
        direction,
        destination_type,
        chained_event_id,
        chained_event_target,
        chained_event_obj):
    """
    Triggered event will additionally contain these attributes:
        negotiated-target-cid
        negotiated-target-parent-cid

    :param source_cid:
    :param direction:
    :param destination_type:
    :param chained_event_id:
    :param chained_event_target:
    :param chained_event_obj:
    :return:
    """
    assert direction in DIRECTIONS
    assert destination_type in DESTINATION_TYPES
    return {
        'source-cid': source_cid,
        'direction': direction,
        'previous-cid': None,
        'origin-portal-cid': source_cid,
        'destination-type': destination_type,
        'chained-event-id': chained_event_id,
        'chained-event-target': chained_event_target,
        'chained-event-obj': chained_event_obj,
    }
