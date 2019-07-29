
from .....system.participant import create_singleton_identity


COMPONENT_ID_CREATE_TEXTBOX = create_singleton_identity('core.platform.api/textbox')

class TextboxCreation:
    """
    Construction object used in the request to create the textbox.
    """


COMPONENT_ID_CREATE_NOTICE = create_singleton_identity('core.platform.api/notice')

class NoticeCreation:
    """
    Construction object used to create a notification.
    """
    