# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia.core.api.portal version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    List,
    Union,
    Any,
    Dict,
    cast,
    SupportsInt,
    Optional,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    STANDARD_PETRONIA_CATALOG,
    StdRet,
    not_none,
    collect_errors_from,
)

EXTENSION_NAME = 'petronia.core.api.portal'
EXTENSION_VERSION = (1, 0, 0)


class ScreenBlock:
    """
    A virtual screen area to match.
    """
    __slots__ = ('x', 'y', 'width', 'height',)

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ScreenBlock']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('x')
        f_x: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='x',
                name='ScreenBlock',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='x',
                    type='int',
                    name='ScreenBlock',
                )
            f_x = int(val)
        val = data.get('y')
        f_y: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='y',
                name='ScreenBlock',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='y',
                    type='int',
                    name='ScreenBlock',
                )
            f_y = int(val)
        val = data.get('width')
        f_width: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='width',
                name='ScreenBlock',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='width',
                    type='int',
                    name='ScreenBlock',
                )
            f_width = int(val)
        val = data.get('height')
        f_height: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='height',
                name='ScreenBlock',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='height',
                    type='int',
                    name='ScreenBlock',
                )
            f_height = int(val)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ScreenBlock(
            x=not_none(f_x),
            y=not_none(f_y),
            width=not_none(f_width),
            height=not_none(f_height),
        ))

    def __repr__(self) -> str:
        return "ScreenBlock(" + repr(self.export_data()) + ")"


class WindowPortalFit:
    """
    How to size the window within the portal. The window can be stretched to fit
    each edge, or resized to be at most the edge length, and aligned at different
    places along the edges.
    """
    __slots__ = ('justify_horizontal', 'justify_vertical', 'fit_horizontal', 'fit_vertical',)

    def __init__(
        self,
        justify_horizontal: str,
        justify_vertical: str,
        fit_horizontal: str,
        fit_vertical: str,
    ) -> None:
        self.justify_horizontal = justify_horizontal
        self.justify_vertical = justify_vertical
        self.fit_horizontal = fit_horizontal
        self.fit_vertical = fit_vertical

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'justify_horizontal': self.justify_horizontal,
            'justify_vertical': self.justify_vertical,
            'fit_horizontal': self.fit_horizontal,
            'fit_vertical': self.fit_vertical,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowPortalFit']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('justify_horizontal')
        f_justify_horizontal: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='justify_horizontal',
                name='WindowPortalFit',
            )
        else:
            if val not in ('right','left','center', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='justify_horizontal',
                    type='str',
                    name='WindowPortalFit',
                )
            f_justify_horizontal = val
        val = data.get('justify_vertical')
        f_justify_vertical: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='justify_vertical',
                name='WindowPortalFit',
            )
        else:
            if val not in ('center','bottom','top', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='justify_vertical',
                    type='str',
                    name='WindowPortalFit',
                )
            f_justify_vertical = val
        val = data.get('fit_horizontal')
        f_fit_horizontal: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='fit_horizontal',
                name='WindowPortalFit',
            )
        else:
            if val not in ('fit','shrink','stretch','none', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='fit_horizontal',
                    type='str',
                    name='WindowPortalFit',
                )
            f_fit_horizontal = val
        val = data.get('fit_vertical')
        f_fit_vertical: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='fit_vertical',
                name='WindowPortalFit',
            )
        else:
            if val not in ('fit','shrink','stretch','none', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='fit_vertical',
                    type='str',
                    name='WindowPortalFit',
                )
            f_fit_vertical = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowPortalFit(
            justify_horizontal=not_none(f_justify_horizontal),
            justify_vertical=not_none(f_justify_vertical),
            fit_horizontal=not_none(f_fit_horizontal),
            fit_vertical=not_none(f_fit_vertical),
        ))

    def __repr__(self) -> str:
        return "WindowPortalFit(" + repr(self.export_data()) + ")"


class Portal:
    """
    A "leaf" within the layout arrangement.
    """
    __slots__ = ('window_ids', 'size', 'preferred_location', 'padding_top', 'padding_bottom', 'padding_left', 'padding_right', 'portal_aliases',)

    def __init__(
        self,
        window_ids: List[str],
        size: int,
        preferred_location: WindowPortalFit,
        padding_top: int,
        padding_bottom: int,
        padding_left: int,
        padding_right: int,
        portal_aliases: List[str],
    ) -> None:
        self.window_ids = window_ids
        self.size = size
        self.preferred_location = preferred_location
        self.padding_top = padding_top
        self.padding_bottom = padding_bottom
        self.padding_left = padding_left
        self.padding_right = padding_right
        self.portal_aliases = portal_aliases

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'window_ids': list(self.window_ids),
            'size': self.size,
            'preferred_location': self.preferred_location.export_data(),
            'padding_top': self.padding_top,
            'padding_bottom': self.padding_bottom,
            'padding_left': self.padding_left,
            'padding_right': self.padding_right,
            'portal_aliases': list(self.portal_aliases),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Portal']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('window_ids')
        f_window_ids: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='window_ids',
                name='Portal',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='window_ids',
                    type='List[str]',
                    name='Portal',
                )
            f_window_ids = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='window_ids',
                        type='str',
                        name='Portal',
                    )
                f_window_ids.append(item)
        val = data.get('size')
        f_size: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='size',
                name='Portal',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='size',
                    type='int',
                    name='Portal',
                )
            f_size = int(val)
        val = data.get('preferred_location')
        f_preferred_location: WindowPortalFit
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='preferred_location',
                name='Portal',
            )
        else:
            parsed_preferred_location = WindowPortalFit.parse_data(val)
            if parsed_preferred_location.has_error:
                return parsed_preferred_location.forward()
            if parsed_preferred_location.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='preferred_location',
                )
            f_preferred_location = parsed_preferred_location.result
        val = data.get('padding_top')
        f_padding_top: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='padding_top',
                name='Portal',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='padding_top',
                    type='int',
                    name='Portal',
                )
            f_padding_top = int(val)
        val = data.get('padding_bottom')
        f_padding_bottom: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='padding_bottom',
                name='Portal',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='padding_bottom',
                    type='int',
                    name='Portal',
                )
            f_padding_bottom = int(val)
        val = data.get('padding_left')
        f_padding_left: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='padding_left',
                name='Portal',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='padding_left',
                    type='int',
                    name='Portal',
                )
            f_padding_left = int(val)
        val = data.get('padding_right')
        f_padding_right: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='padding_right',
                name='Portal',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='padding_right',
                    type='int',
                    name='Portal',
                )
            f_padding_right = int(val)
        val = data.get('portal_aliases')
        f_portal_aliases: List[str]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='portal_aliases',
                name='Portal',
            )
        else:
            if not isinstance(val, list):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='portal_aliases',
                    type='List[str]',
                    name='Portal',
                )
            f_portal_aliases = []
            for item in val:
                if not isinstance(item, str):
                    return StdRet.pass_errmsg(
                        STANDARD_PETRONIA_CATALOG,
                        _(
                            'Field {field_name} must contain items '
                            'of type {type} for structure {name}'
                        ),
                        field_name='portal_aliases',
                        type='str',
                        name='Portal',
                    )
                f_portal_aliases.append(item)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Portal(
            window_ids=not_none(f_window_ids),
            size=not_none(f_size),
            preferred_location=not_none(f_preferred_location),
            padding_top=not_none(f_padding_top),
            padding_bottom=not_none(f_padding_bottom),
            padding_left=not_none(f_padding_left),
            padding_right=not_none(f_padding_right),
            portal_aliases=not_none(f_portal_aliases),
        ))

    def __repr__(self) -> str:
        return "Portal(" + repr(self.export_data()) + ")"


class SplitContent:
    """
    The contents of a cell within a layout split.
    """
    __slots__ = ('__name', '__value')

    def __init__(
        self,
        name: str,
        value: Union[
            LayoutSplit,
            Portal,
        ],
    ) -> None:
        self.__name = name
        self.__value = value

    @property
    def name(self) -> str:
        """Name of the selector type."""
        return self.__name

    @property
    def value(self) -> Union[
            LayoutSplit,
            Portal,
    ]:
        """The selector value."""
        return self.__value

    def __repr__(self) -> str:
        return 'SplitContent(type: {0}, value: {1})'.format(
            self.__name, repr(self.__value),
        )

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0912
        """Create the event data structure, ready for marshalling."""
        if self.__name == 'split':
            return {
                '^': self.__name,
                '$':
                    self.__value.export_data(),
            }
        if self.__name == 'portal':
            return {
                '^': self.__name,
                '$':
                    self.__value.export_data(),
            }
        raise RuntimeError('invalid inner type: ' + repr(self.__name))  # pragma no cover

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SplitContent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        selector_name = data.get('^')
        val = data.get('$')
        if not isinstance(selector_name, str):
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('selector value must have ^ and $ keys'),
            )
        if selector_name == 'split':
            if not isinstance(val, dict):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must be a mapping '
                        'for structure {name}'
                    ),
                    field_name='split',
                    name='SplitContent',
                )
            parsed_val_LayoutSplit = LayoutSplit.parse_data(val)
            if parsed_val_LayoutSplit.has_error:
                return parsed_val_LayoutSplit.forward()
            return StdRet.pass_ok(SplitContent(
                selector_name,
                parsed_val_LayoutSplit.result,
            ))
        if selector_name == 'portal':
            if not isinstance(val, dict):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must be a mapping '
                        'for structure {name}'
                    ),
                    field_name='portal',
                    name='SplitContent',
                )
            parsed_val_Portal = Portal.parse_data(val)
            if parsed_val_Portal.has_error:
                return parsed_val_Portal.forward()
            return StdRet.pass_ok(SplitContent(
                selector_name,
                parsed_val_Portal.result,
            ))
        return StdRet.pass_errmsg(
            STANDARD_PETRONIA_CATALOG,
            _('Invalid selector name {name} for {nc}'),
            name=selector_name,
            nc='SplitContent',
        )


class LayoutSplit:
    """
    A divider for the layout. A split contains 1 or more other splits or portals.
    Each layered split alternates the split direction.
    """
    __slots__ = ('size', 'direction', 'contents',)

    def __init__(
        self,
        size: int,
        direction: str,
        contents: List[SplitContent],
    ) -> None:
        self.size = size
        self.direction = direction
        self.contents = contents

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'size': self.size,
            'direction': self.direction,
            'contents': [v.export_data() for v in self.contents],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['LayoutSplit']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('size')
        f_size: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='size',
                name='LayoutSplit',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='size',
                    type='int',
                    name='LayoutSplit',
                )
            f_size = int(val)
        val = data.get('direction')
        f_direction: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='direction',
                name='LayoutSplit',
            )
        else:
            if val not in ('horizontal','vertical', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='direction',
                    type='str',
                    name='LayoutSplit',
                )
            f_direction = val
        val = data.get('contents')
        f_contents: List[SplitContent]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='contents',
                name='LayoutSplit',
            )
        else:
            f_contents = []
            for item in val:
                parsed_contents = SplitContent.parse_data(item)
                if parsed_contents.has_error:
                    return parsed_contents.forward()
                f_contents.append(parsed_contents.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(LayoutSplit(
            size=not_none(f_size),
            direction=not_none(f_direction),
            contents=not_none(f_contents),
        ))

    def __repr__(self) -> str:
        return "LayoutSplit(" + repr(self.export_data()) + ")"


class ScreenMatcher:
    """
    A rough description of the virtual screen space, and the associated layout.
    """
    __slots__ = ('block', 'layout',)

    def __init__(
        self,
        block: ScreenBlock,
        layout: LayoutSplit,
    ) -> None:
        self.block = block
        self.layout = layout

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'block': self.block.export_data(),
            'layout': self.layout.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ScreenMatcher']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('block')
        f_block: ScreenBlock
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='block',
                name='ScreenMatcher',
            )
        else:
            parsed_block = ScreenBlock.parse_data(val)
            if parsed_block.has_error:
                return parsed_block.forward()
            if parsed_block.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='block',
                )
            f_block = parsed_block.result
        val = data.get('layout')
        f_layout: LayoutSplit
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='layout',
                name='ScreenMatcher',
            )
        else:
            parsed_layout = LayoutSplit.parse_data(val)
            if parsed_layout.has_error:
                return parsed_layout.forward()
            if parsed_layout.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='layout',
                )
            f_layout = parsed_layout.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ScreenMatcher(
            block=not_none(f_block),
            layout=not_none(f_layout),
        ))

    def __repr__(self) -> str:
        return "ScreenMatcher(" + repr(self.export_data()) + ")"


class WorkspaceSetup:
    """
    A layout with an optional screen size it associates with. The workspace that
    does not have a screen matcher is considered the "default" workspace.
    """
    __slots__ = ('screens',)

    def __init__(
        self,
        screens: List[ScreenMatcher],
    ) -> None:
        self.screens = screens

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'screens': [v.export_data() for v in self.screens],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WorkspaceSetup']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('screens')
        f_screens: List[ScreenMatcher]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='screens',
                name='WorkspaceSetup',
            )
        else:
            f_screens = []
            for item in val:
                parsed_screens = ScreenMatcher.parse_data(item)
                if parsed_screens.has_error:
                    return parsed_screens.forward()
                f_screens.append(parsed_screens.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WorkspaceSetup(
            screens=not_none(f_screens),
        ))

    def __repr__(self) -> str:
        return "WorkspaceSetup(" + repr(self.export_data()) + ")"


class SetLayoutEvent:
    """
    Set the current layout. Changes the entire setup.
    """
    __slots__ = ('workspace',)
    FULL_EVENT_NAME = 'petronia.core.api.portal:set-layout'
    SHORT_EVENT_NAME = 'set-layout'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:layout'
    UNIQUE_TARGET_REL = 'layout'

    def __init__(
        self,
        workspace: WorkspaceSetup,
    ) -> None:
        self.workspace = workspace

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SetLayoutEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'workspace': self.workspace.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SetLayoutEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('workspace')
        f_workspace: WorkspaceSetup
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='workspace',
                name='SetLayoutEvent',
            )
        else:
            parsed_workspace = WorkspaceSetup.parse_data(val)
            if parsed_workspace.has_error:
                return parsed_workspace.forward()
            if parsed_workspace.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='workspace',
                )
            f_workspace = parsed_workspace.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SetLayoutEvent(
            workspace=not_none(f_workspace),
        ))

    def __repr__(self) -> str:
        return "SetLayoutEvent(" + repr(self.export_data()) + ")"


class SplitPortalEvent:
    """
    Splits the active portal into two portals.
    """
    __slots__ = ('add_before', 'focus_new', 'new_direction',)
    FULL_EVENT_NAME = 'petronia.core.api.portal:split-portal'
    SHORT_EVENT_NAME = 'split-portal'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-portal'
    UNIQUE_TARGET_REL = 'active-portal'

    def __init__(
        self,
        add_before: bool,
        focus_new: bool,
        new_direction: bool,
    ) -> None:
        self.add_before = add_before
        self.focus_new = focus_new
        self.new_direction = new_direction

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return SplitPortalEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'add_before': self.add_before,
            'focus_new': self.focus_new,
            'new_direction': self.new_direction,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['SplitPortalEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('add_before')
        f_add_before: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='add_before',
                name='SplitPortalEvent',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='add_before',
                    type='bool',
                    name='SplitPortalEvent',
                )
            f_add_before = val
        val = data.get('focus_new')
        f_focus_new: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='focus_new',
                name='SplitPortalEvent',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='focus_new',
                    type='bool',
                    name='SplitPortalEvent',
                )
            f_focus_new = val
        val = data.get('new_direction')
        f_new_direction: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='new_direction',
                name='SplitPortalEvent',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='new_direction',
                    type='bool',
                    name='SplitPortalEvent',
                )
            f_new_direction = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(SplitPortalEvent(
            add_before=not_none(f_add_before),
            focus_new=not_none(f_focus_new),
            new_direction=not_none(f_new_direction),
        ))

    def __repr__(self) -> str:
        return "SplitPortalEvent(" + repr(self.export_data()) + ")"


class JoinPortalsEvent:
    """
    Joins the active portal with its neighbor. The currently focused window will
    remain in-focus. The order of the joined windows is left up to the
    implementation.
    """
    __slots__ = ('join_before',)
    FULL_EVENT_NAME = 'petronia.core.api.portal:join-portals'
    SHORT_EVENT_NAME = 'join-portals'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-portal'
    UNIQUE_TARGET_REL = 'active-portal'

    def __init__(
        self,
        join_before: bool,
    ) -> None:
        self.join_before = join_before

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return JoinPortalsEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'join_before': self.join_before,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['JoinPortalsEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('join_before')
        f_join_before: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='join_before',
                name='JoinPortalsEvent',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='join_before',
                    type='bool',
                    name='JoinPortalsEvent',
                )
            f_join_before = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(JoinPortalsEvent(
            join_before=not_none(f_join_before),
        ))

    def __repr__(self) -> str:
        return "JoinPortalsEvent(" + repr(self.export_data()) + ")"


class FitWindowEvent:
    """
    Change the active window positioning within the portal. If there are multiple
    windows within the portal, only the active is changed.
    """
    __slots__ = ('position',)
    FULL_EVENT_NAME = 'petronia.core.api.portal:fit-window'
    SHORT_EVENT_NAME = 'fit-window'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-window'
    UNIQUE_TARGET_REL = 'active-window'

    def __init__(
        self,
        position: WindowPortalFit,
    ) -> None:
        self.position = position

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return FitWindowEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'position': self.position.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['FitWindowEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('position')
        f_position: WindowPortalFit
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='position',
                name='FitWindowEvent',
            )
        else:
            parsed_position = WindowPortalFit.parse_data(val)
            if parsed_position.has_error:
                return parsed_position.forward()
            if parsed_position.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='position',
                )
            f_position = parsed_position.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(FitWindowEvent(
            position=not_none(f_position),
        ))

    def __repr__(self) -> str:
        return "FitWindowEvent(" + repr(self.export_data()) + ")"


class FitPortalWindowsEvent:
    """
    Change the focused portal's contained window positioning. This changes only the
    default setting; windows that have an explicit position set will not be
    affected.
    """
    __slots__ = ('position',)
    FULL_EVENT_NAME = 'petronia.core.api.portal:fit-portal-windows'
    SHORT_EVENT_NAME = 'fit-portal-windows'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-portal'
    UNIQUE_TARGET_REL = 'active-portal'

    def __init__(
        self,
        position: WindowPortalFit,
    ) -> None:
        self.position = position

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return FitPortalWindowsEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'position': self.position.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['FitPortalWindowsEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('position')
        f_position: WindowPortalFit
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='position',
                name='FitPortalWindowsEvent',
            )
        else:
            parsed_position = WindowPortalFit.parse_data(val)
            if parsed_position.has_error:
                return parsed_position.forward()
            if parsed_position.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='position',
                )
            f_position = parsed_position.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(FitPortalWindowsEvent(
            position=not_none(f_position),
        ))

    def __repr__(self) -> str:
        return "FitPortalWindowsEvent(" + repr(self.export_data()) + ")"


class ManageWindowEvent:
    """
    Take control of the active window, putting it in the focused portal.
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.portal:manage-window'
    SHORT_EVENT_NAME = 'manage-window'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-window'
    UNIQUE_TARGET_REL = 'active-window'

    def __init__(
        self,
    ) -> None:
        pass

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return ManageWindowEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {}

    @staticmethod
    def parse_data(_data: Dict[str, Any]) -> StdRet['ManageWindowEvent']:
        """Parse the marshalled data into this structured form.  There are no fields, so this is
        essentially a no-op."""
        return StdRet.pass_ok(ManageWindowEvent())

    def __repr__(self) -> str:
        return "ManageWindowEvent(" + repr(self.export_data()) + ")"


class UnmanageWindowEvent:
    """
    Release Petronia control of the active window, allowing it to be a "floating"
    window.
    """
    __slots__ = ()
    FULL_EVENT_NAME = 'petronia.core.api.portal:unmanage-window'
    SHORT_EVENT_NAME = 'unmanage-window'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-window'
    UNIQUE_TARGET_REL = 'active-window'

    def __init__(
        self,
    ) -> None:
        pass

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return UnmanageWindowEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        return {}

    @staticmethod
    def parse_data(_data: Dict[str, Any]) -> StdRet['UnmanageWindowEvent']:
        """Parse the marshalled data into this structured form.  There are no fields, so this is
        essentially a no-op."""
        return StdRet.pass_ok(UnmanageWindowEvent())

    def __repr__(self) -> str:
        return "UnmanageWindowEvent(" + repr(self.export_data()) + ")"


class AdjustPortalSizeEvent:
    """
    Changes the size of the portal. If the size change direction is not in the split
    direction (e.g. the portals are split vertically, but a request to change the
    horizontal size), then the owning split's size is changed. The change is
    relative to the current size.
    """
    __slots__ = ('amount', 'direction',)
    FULL_EVENT_NAME = 'petronia.core.api.portal:adjust-portal-size'
    SHORT_EVENT_NAME = 'adjust-portal-size'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-portal'
    UNIQUE_TARGET_REL = 'active-portal'

    def __init__(
        self,
        amount: int,
        direction: str,
    ) -> None:
        self.amount = amount
        self.direction = direction

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return AdjustPortalSizeEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'amount': self.amount,
            'direction': self.direction,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['AdjustPortalSizeEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('amount')
        f_amount: int
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='amount',
                name='AdjustPortalSizeEvent',
            )
        else:
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='amount',
                    type='int',
                    name='AdjustPortalSizeEvent',
                )
            f_amount = int(val)
        val = data.get('direction')
        f_direction: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='direction',
                name='AdjustPortalSizeEvent',
            )
        else:
            if val not in ('horizontal','vertical', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='direction',
                    type='str',
                    name='AdjustPortalSizeEvent',
                )
            f_direction = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(AdjustPortalSizeEvent(
            amount=not_none(f_amount),
            direction=not_none(f_direction),
        ))

    def __repr__(self) -> str:
        return "AdjustPortalSizeEvent(" + repr(self.export_data()) + ")"


class MarkPortalEvent:
    """
    Mark the active portal with an identifier. This can be used for quick window
    moves or focus later.
    """
    __slots__ = ('name',)
    FULL_EVENT_NAME = 'petronia.core.api.portal:mark-portal'
    SHORT_EVENT_NAME = 'mark-portal'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-portal'
    UNIQUE_TARGET_REL = 'active-portal'

    def __init__(
        self,
        name: str,
    ) -> None:
        self.name = name

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return MarkPortalEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'name': self.name,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['MarkPortalEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('name')
        f_name: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='name',
                name='MarkPortalEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='name',
                    type='str',
                    name='MarkPortalEvent',
                )
            f_name = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(MarkPortalEvent(
            name=not_none(f_name),
        ))

    def __repr__(self) -> str:
        return "MarkPortalEvent(" + repr(self.export_data()) + ")"


class MoveWindowToPortalEvent:
    """
    Move the active window to another portal. This can be either relative or by
    name.
    """
    __slots__ = ('target', 'move_focus', 'wrap',)
    FULL_EVENT_NAME = 'petronia.core.api.portal:move-window-to-portal'
    SHORT_EVENT_NAME = 'move-window-to-portal'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-window'
    UNIQUE_TARGET_REL = 'active-window'

    def __init__(
        self,
        target: str,
        move_focus: bool,
        wrap: str,
    ) -> None:
        self.target = target
        self.move_focus = move_focus
        self.wrap = wrap

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return MoveWindowToPortalEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'target': self.target,
            'move_focus': self.move_focus,
            'wrap': self.wrap,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['MoveWindowToPortalEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('target')
        f_target: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='target',
                name='MoveWindowToPortalEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='target',
                    type='str',
                    name='MoveWindowToPortalEvent',
                )
            f_target = val
        val = data.get('move_focus')
        f_move_focus: bool
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='move_focus',
                name='MoveWindowToPortalEvent',
            )
        else:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='move_focus',
                    type='bool',
                    name='MoveWindowToPortalEvent',
                )
            f_move_focus = val
        val = data.get('wrap')
        f_wrap: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='wrap',
                name='MoveWindowToPortalEvent',
            )
        else:
            if val not in ('wrap-screen','wrap-block','none', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='wrap',
                    type='str',
                    name='MoveWindowToPortalEvent',
                )
            f_wrap = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(MoveWindowToPortalEvent(
            target=not_none(f_target),
            move_focus=not_none(f_move_focus),
            wrap=not_none(f_wrap),
        ))

    def __repr__(self) -> str:
        return "MoveWindowToPortalEvent(" + repr(self.export_data()) + ")"


class FocusPortalEvent:
    """
    Moves the currently focused portal to another portal. The target portal can
    either be one of the reserved direction names, or a marked portal name. The
    currently "top" window in the focused portal will become the new active window.
    """
    __slots__ = ('target', 'wrap',)
    FULL_EVENT_NAME = 'petronia.core.api.portal:focus-portal'
    SHORT_EVENT_NAME = 'focus-portal'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-portal'
    UNIQUE_TARGET_REL = 'active-portal'

    def __init__(
        self,
        target: str,
        wrap: str,
    ) -> None:
        self.target = target
        self.wrap = wrap

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return FocusPortalEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'target': self.target,
            'wrap': self.wrap,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['FocusPortalEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('target')
        f_target: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='target',
                name='FocusPortalEvent',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='target',
                    type='str',
                    name='FocusPortalEvent',
                )
            f_target = val
        val = data.get('wrap')
        f_wrap: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='wrap',
                name='FocusPortalEvent',
            )
        else:
            if val not in ('wrap-screen','wrap-block','none', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='wrap',
                    type='str',
                    name='FocusPortalEvent',
                )
            f_wrap = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(FocusPortalEvent(
            target=not_none(f_target),
            wrap=not_none(f_wrap),
        ))

    def __repr__(self) -> str:
        return "FocusPortalEvent(" + repr(self.export_data()) + ")"


class RotateActiveWindowEvent:
    """
    For the active portal, rotate which window is "on top". If the portal has zero
    or one window, then this event does nothing.
    """
    __slots__ = ('direction',)
    FULL_EVENT_NAME = 'petronia.core.api.portal:rotate-active-window'
    SHORT_EVENT_NAME = 'rotate-active-window'

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-portal'
    UNIQUE_TARGET_REL = 'active-portal'

    def __init__(
        self,
        direction: str,
    ) -> None:
        self.direction = direction

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return RotateActiveWindowEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'direction': self.direction,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['RotateActiveWindowEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('direction')
        f_direction: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='direction',
                name='RotateActiveWindowEvent',
            )
        else:
            if val not in ('backward','forward', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='direction',
                    type='str',
                    name='RotateActiveWindowEvent',
                )
            f_direction = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(RotateActiveWindowEvent(
            direction=not_none(f_direction),
        ))

    def __repr__(self) -> str:
        return "RotateActiveWindowEvent(" + repr(self.export_data()) + ")"


class WorkspaceConfigurationState:
    """
    Collection of layouts, mapping to different virtual screen arrangements. The
    best fitting layout for the active virtual screen will be used.
    """
    __slots__ = ('workspaces',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:workspace-configuration'
    UNIQUE_TARGET_REL = 'petronia.core.api.portal:workspace-configuration'

    def __init__(
        self,
        workspaces: List[WorkspaceSetup],
    ) -> None:
        self.workspaces = workspaces

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'workspaces': [v.export_data() for v in self.workspaces],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WorkspaceConfigurationState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('workspaces')
        f_workspaces: List[WorkspaceSetup]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='workspaces',
                name='WorkspaceConfigurationState',
            )
        else:
            f_workspaces = []
            for item in val:
                parsed_workspaces = WorkspaceSetup.parse_data(item)
                if parsed_workspaces.has_error:
                    return parsed_workspaces.forward()
                f_workspaces.append(parsed_workspaces.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WorkspaceConfigurationState(
            workspaces=not_none(f_workspaces),
        ))

    def __repr__(self) -> str:
        return "WorkspaceConfigurationState(" + repr(self.export_data()) + ")"


class ActiveLayoutState:
    """
    The currently active layout. As the split and join events are called, and
    windows are moved between portals, this will be updated to reflect the current
    arrangement. The layout is matched up with the active virtual screen.
    """
    __slots__ = ('workspace',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:active-layout'
    UNIQUE_TARGET_REL = 'petronia.core.api.portal:active-layout'

    def __init__(
        self,
        workspace: WorkspaceSetup,
    ) -> None:
        self.workspace = workspace

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'workspace': self.workspace.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ActiveLayoutState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('workspace')
        f_workspace: WorkspaceSetup
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='workspace',
                name='ActiveLayoutState',
            )
        else:
            parsed_workspace = WorkspaceSetup.parse_data(val)
            if parsed_workspace.has_error:
                return parsed_workspace.forward()
            if parsed_workspace.value is None:
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _(
                        'Field {field_name} must not be null'
                    ),
                    field_name='workspace',
                )
            f_workspace = parsed_workspace.result
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ActiveLayoutState(
            workspace=not_none(f_workspace),
        ))

    def __repr__(self) -> str:
        return "ActiveLayoutState(" + repr(self.export_data()) + ")"


class FocusState:
    """
    The currently focused portal and window.
    """
    __slots__ = ('portal_name', 'window_id',)

    UNIQUE_TARGET_FQN = 'petronia.core.api.portal:focus'
    UNIQUE_TARGET_REL = 'petronia.core.api.portal:focus'

    def __init__(
        self,
        portal_name: str,
        window_id: Optional[str],
    ) -> None:
        self.portal_name = portal_name
        self.window_id = window_id

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'portal_name': self.portal_name,
            'window_id': self.window_id,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['FocusState']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('portal_name')
        f_portal_name: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='portal_name',
                name='FocusState',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='portal_name',
                    type='str',
                    name='FocusState',
                )
            f_portal_name = val
        val = data.get('window_id')
        f_window_id: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='window_id',
                    type='str',
                    name='FocusState',
                )
            f_window_id = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(FocusState(
            portal_name=not_none(f_portal_name),
            window_id=f_window_id,
        ))

    def __repr__(self) -> str:
        return "FocusState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
