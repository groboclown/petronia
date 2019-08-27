
"""
Custom GUI Notification pop-ups.
"""

from .....base import create_singleton_identity


COMPONENT_FACTORY_ID_NOTICE = create_singleton_identity('core.platform.api/notice')


class NoticeCreation:
    """
    Details for a new notification.
    Pass to RequestNewComponentEvent.
    """


class NotificationAreaCreation:
    """
    Details for a new area where notifications are displayed.
    Pass to RequestNewComponentEvent.
    """
