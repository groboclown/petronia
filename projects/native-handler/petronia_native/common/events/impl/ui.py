# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia.core.api.native.ui version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name,consider-using-f-string

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Dict,
    SupportsInt,
    List,
    cast,
    Any,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    not_none,
    STANDARD_PETRONIA_CATALOG,
    collect_errors_from,
    StdRet,
)

EXTENSION_NAME = 'petronia.core.api.native.ui'
EXTENSION_VERSION = (1, 0, 0)


class RegisterImageDetailsEvent:
    """
    Register an image for display. This must be followed up with a
    register-image-bytes event. The source ID is the image registration ID.
    """
    __slots__ = ('locale', 'format',)
    FULL_EVENT_NAME = 'petronia.core.api.native.ui:register-image-details'
    SHORT_EVENT_NAME = 'register-image-details'

    def __init__(
        self,
        locale: str,
        format: str,
    ) -> None:
        self.locale = locale
        self.format = format

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return RegisterImageDetailsEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'locale': self.locale,
            'format': self.format,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['RegisterImageDetailsEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('locale')
        f_locale: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='locale',
                name='RegisterImageDetailsEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='locale',
                    type='str',
                    name='RegisterImageDetailsEvent',
                )
            f_locale = val
        val = data.get('format')
        f_format: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='format',
                name='RegisterImageDetailsEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='format',
                    type='str',
                    name='RegisterImageDetailsEvent',
                )
            f_format = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(RegisterImageDetailsEvent(
            locale=not_none(f_locale),
            format=not_none(f_format),
        ))

    def __repr__(self) -> str:
        return "RegisterImageDetailsEvent(" + repr(self.export_data()) + ")"


class UiPanelClickedEvent:
    """
    A UI panel was clicked on.
    """
    __slots__ = ('identifier', 'mouse_buttons',)
    FULL_EVENT_NAME = 'petronia.core.api.native.ui:ui-panel-clicked'
    SHORT_EVENT_NAME = 'ui-panel-clicked'

    def __init__(
        self,
        identifier: int,
        mouse_buttons: List[int],
    ) -> None:
        self.identifier = identifier
        self.mouse_buttons = mouse_buttons

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return UiPanelClickedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'mouse_buttons': list(self.mouse_buttons),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['UiPanelClickedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('identifier')
        f_identifier: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='identifier',
                name='UiPanelClickedEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='int',
                    name='UiPanelClickedEvent',
                )
            f_identifier = int(val)
        val = data.get('mouse_buttons')
        f_mouse_buttons: List[int]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='mouse_buttons',
                name='UiPanelClickedEvent',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='mouse_buttons',
                    type='List[int]',
                    name='UiPanelClickedEvent',
                )
            f_mouse_buttons = []
            for item in val:
                if not isinstance(item, int):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='mouse_buttons',
                        type='int',
                        name='UiPanelClickedEvent',
                    )
                f_mouse_buttons.append(item)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(UiPanelClickedEvent(
            identifier=not_none(f_identifier),
            mouse_buttons=not_none(f_mouse_buttons),
        ))

    def __repr__(self) -> str:
        return "UiPanelClickedEvent(" + repr(self.export_data()) + ")"


class UiTextFieldUpdateEvent:
    """
    Text inside a text field UI element changed.
    """
    __slots__ = ('identifier', 'text',)
    FULL_EVENT_NAME = 'petronia.core.api.native.ui:ui-text-field-update'
    SHORT_EVENT_NAME = 'ui-text-field-update'

    def __init__(
        self,
        identifier: int,
        text: str,
    ) -> None:
        self.identifier = identifier
        self.text = text

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return UiTextFieldUpdateEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'text': self.text,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['UiTextFieldUpdateEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('identifier')
        f_identifier: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='identifier',
                name='UiTextFieldUpdateEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='int',
                    name='UiTextFieldUpdateEvent',
                )
            f_identifier = int(val)
        val = data.get('text')
        f_text: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='text',
                name='UiTextFieldUpdateEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='text',
                    type='str',
                    name='UiTextFieldUpdateEvent',
                )
            f_text = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(UiTextFieldUpdateEvent(
            identifier=not_none(f_identifier),
            text=not_none(f_text),
        ))

    def __repr__(self) -> str:
        return "UiTextFieldUpdateEvent(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
