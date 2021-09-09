# GENERATED CODE - DO NOT MODIFY

"""
Data structures and marshalling for extension petronia_portal version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics
# pylint:disable=too-many-lines,line-too-long,too-many-arguments,too-many-statements,too-many-return-statements,too-many-instance-attributes,too-few-public-methods,unused-import,invalid-name

# Allow forward references and thus cyclic data types
from __future__ import annotations
from typing import (
    Union,
    Any,
    SupportsInt,
    List,
    Optional,
    Dict,
    cast,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    collect_errors_from,
    StdRet,
    STANDARD_PETRONIA_CATALOG,
    not_none,
)

EXTENSION_NAME = 'petronia_portal'
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
            if val not in ('top','bottom','center', ):
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
            if val not in ('shrink','stretch','fit','none', ):
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
            if val not in ('shrink','stretch','fit','none', ):
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
    __slots__ = ('size', 'preferred_location', 'padding_top', 'padding_bottom', 'padding_left', 'padding_right', 'portal_aliases',)

    def __init__(
        self,
        size: int,
        preferred_location: WindowPortalFit,
        padding_top: int,
        padding_bottom: int,
        padding_left: int,
        padding_right: int,
        portal_aliases: List[str],
    ) -> None:
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


class WindowMatchItem:
    """
    A single meta-data matcher for a window.
    """
    __slots__ = ('key', 'match_type', 'value',)

    def __init__(
        self,
        key: str,
        match_type: str,
        value: str,
    ) -> None:
        self.key = key
        self.match_type = match_type
        self.value = value

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'key': self.key,
            'match_type': self.match_type,
            'value': self.value,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowMatchItem']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('key')
        f_key: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='key',
                name='WindowMatchItem',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='key',
                    type='str',
                    name='WindowMatchItem',
                )
            f_key = val
        val = data.get('match_type')
        f_match_type: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='match_type',
                name='WindowMatchItem',
            )
        else:
            if val not in ('regex','glob','exists','exact','not-exists', ):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='match_type',
                    type='str',
                    name='WindowMatchItem',
                )
            f_match_type = val
        val = data.get('value')
        f_value: str
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='value',
                name='WindowMatchItem',
            )
        else:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='value',
                    type='str',
                    name='WindowMatchItem',
                )
            f_value = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowMatchItem(
            key=not_none(f_key),
            match_type=not_none(f_match_type),
            value=not_none(f_value),
        ))

    def __repr__(self) -> str:
        return "WindowMatchItem(" + repr(self.export_data()) + ")"


class WindowMatch:
    """
    Matches a window description to a default assigned portal and fit.
    """
    __slots__ = ('match', 'managed', 'fit', 'initial_portal',)

    def __init__(
        self,
        match: List[WindowMatchItem],
        managed: Optional[bool],
        fit: Optional[WindowPortalFit],
        initial_portal: Optional[str],
    ) -> None:
        self.match = match
        self.managed = managed
        self.fit = fit
        self.initial_portal = initial_portal

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'match': [v.export_data() for v in self.match],
            'managed': self.managed,
            'fit': None if self.fit is None else self.fit.export_data(),
            'initial_portal': self.initial_portal,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['WindowMatch']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        val = data.get('match')
        f_match: List[WindowMatchItem]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='match',
                name='WindowMatch',
            )
        else:
            f_match = []
            for item in val:
                parsed_match = WindowMatchItem.parse_data(item)
                if parsed_match.has_error:
                    return parsed_match.forward()
                f_match.append(parsed_match.result)
        val = data.get('managed')
        f_managed: Optional[bool] = None
        if val is not None:
            if not isinstance(val, bool):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='managed',
                    type='bool',
                    name='WindowMatch',
                )
            f_managed = val
        val = data.get('fit')
        f_fit: Optional[WindowPortalFit] = None
        if val is not None:
            parsed_fit = WindowPortalFit.parse_data(val)
            if parsed_fit.has_error:
                return parsed_fit.forward()
            # Value, not result, because it could be optional...
            f_fit = parsed_fit.value
        val = data.get('initial_portal')
        f_initial_portal: Optional[str] = None
        if val is not None:
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    STANDARD_PETRONIA_CATALOG,
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='initial_portal',
                    type='str',
                    name='WindowMatch',
                )
            f_initial_portal = val
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(WindowMatch(
            match=not_none(f_match),
            managed=f_managed,
            fit=f_fit,
            initial_portal=f_initial_portal,
        ))

    def __repr__(self) -> str:
        return "WindowMatch(" + repr(self.export_data()) + ")"


class ConfigurationState:
    """
    Configuration for the portals.
    """
    __slots__ = ('workspaces', 'default_window_behavior',)

    UNIQUE_TARGET_FQN = 'petronia_portal:configuration'
    UNIQUE_TARGET_REL = 'petronia_portal:configuration'

    def __init__(
        self,
        workspaces: List[WorkspaceSetup],
        default_window_behavior: List[WindowMatch],
    ) -> None:
        self.workspaces = workspaces
        self.default_window_behavior = default_window_behavior

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'workspaces': [v.export_data() for v in self.workspaces],
            'default_window_behavior': [v.export_data() for v in self.default_window_behavior],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['ConfigurationState']:  # pylint: disable=R0912,R0911
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
                name='ConfigurationState',
            )
        else:
            f_workspaces = []
            for item in val:
                parsed_workspaces = WorkspaceSetup.parse_data(item)
                if parsed_workspaces.has_error:
                    return parsed_workspaces.forward()
                f_workspaces.append(parsed_workspaces.result)
        val = data.get('default_window_behavior')
        f_default_window_behavior: List[WindowMatch]
        if val is None:  # pylint:disable=no-else-return
            return StdRet.pass_errmsg(
                STANDARD_PETRONIA_CATALOG,
                _('Required field {field_name} in {name}'),
                field_name='default_window_behavior',
                name='ConfigurationState',
            )
        else:
            f_default_window_behavior = []
            for item in val:
                parsed_default_window_behavior = WindowMatch.parse_data(item)
                if parsed_default_window_behavior.has_error:
                    return parsed_default_window_behavior.forward()
                f_default_window_behavior.append(parsed_default_window_behavior.result)
        if errors:
            return StdRet.pass_error(not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(ConfigurationState(
            workspaces=not_none(f_workspaces),
            default_window_behavior=not_none(f_default_window_behavior),
        ))

    def __repr__(self) -> str:
        return "ConfigurationState(" + repr(self.export_data()) + ")"


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
