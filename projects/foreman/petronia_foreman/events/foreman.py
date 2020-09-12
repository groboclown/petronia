# GENERATED CODE - DO NOT MODIFY
# Created on 2020-09-12T00:48:26.849351

"""
Data structures and marshalling for extension petronia.core.api.foreman version 1.0.0.
"""

# mypy: allow-any-expr,allow-any-decorated,allow-any-explicit,allow-any-generics


from typing import (
    Optional,
    Union,
    Any,
    SupportsInt,
    SupportsFloat,
    Dict,
    List,
)
from petronia_common.util import i18n as _
from petronia_common.util import (
    StdRet,
    T,
    collect_errors_from,
)


class StartLauncherStartedEvent:
    """
    Report that a new launcher now exists and is ready to accept extensions.
    """
    __slots__ = ('identifier',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:start-launcher:started'
    SHORT_EVENT_NAME = 'start-launcher:started'

    def __init__(
        self,
        identifier: str,
    ) -> None:
        self.identifier = identifier

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StartLauncherStartedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['StartLauncherStartedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_identifier: Optional[str] = None
        val = data.get('identifier')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='identifier',
                name='StartLauncherStartedEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='str',
                    name='StartLauncherStartedEvent',
                ))
            else:
                f_identifier = val
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(StartLauncherStartedEvent(
            identifier=_not_none(f_identifier),
        ))

    def __repr__(self) -> str:
        return "StartLauncherStartedEvent(" + repr(self.export_data()) + ")"


class Arguments:
    """
    (no description)
    """
    __slots__ = ('__name', '__value')

    def __init__(
        self,
        name: str,
        value: Union[
            float,
            int,
            str,
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
            float,
            int,
            str,
    ]:
        """The selector value."""
        return self.__value

    def __repr__(self) -> str:
        return 'Arguments(type: {0}, value: {1})'.format(
            self.__name, repr(self.__value),
        )

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0912
        """Create the event data structure, ready for marshalling."""
        if self.__name == 'string':
            return {
                '^': self.__name,
                '$':
                    self.__value,
            }
        if self.__name == 'int':
            return {
                '^': self.__name,
                '$':
                    self.__value,
            }
        if self.__name == 'float':
            return {
                '^': self.__name,
                '$':
                    self.__value,
            }
        raise RuntimeError('invalid inner type: ' + repr(self.__name))  # pragma no cover

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Arguments']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        selector_name = data.get('^')
        val = data.get('$')
        if not isinstance(selector_name, str):
            return StdRet.pass_errmsg(
                _('selector value must have ^ and $ keys'),
            )
        if selector_name == 'string':
            if not isinstance(val, str):
                return StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='string',
                    type='str',
                    name='Arguments',
                )
            return StdRet.pass_ok(Arguments(
                selector_name,
                val,
            ))
        if selector_name == 'int':
            if not isinstance(val, SupportsInt):
                return StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='int',
                    type='int',
                    name='Arguments',
                )
            return StdRet.pass_ok(Arguments(
                selector_name,
                int(val),
            ))
        if selector_name == 'float':
            if not isinstance(val, SupportsFloat):
                return StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='float',
                    type='float',
                    name='Arguments',
                )
            return StdRet.pass_ok(Arguments(
                selector_name,
                float(val),
            ))
        return StdRet.pass_errmsg(
            _('Invalid selector name {name} for {nc}'),
            name=selector_name,
            nc='Arguments',
        )


class Error:
    """
    A failure
    """
    __slots__ = ('identifier', 'source', 'message', 'arguments',)

    def __init__(
        self,
        identifier: str,
        source: Optional[str],
        message: str,
        arguments: List[Arguments],
    ) -> None:
        self.identifier = identifier
        self.source = source
        self.message = message
        self.arguments = arguments

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'source': self.source,
            'message': self.message,
            'arguments': [v.export_data() for v in self.arguments],
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['Error']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_identifier: Optional[str] = None
        val = data.get('identifier')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='identifier',
                name='Error',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='str',
                    name='Error',
                ))
            else:
                f_identifier = val
        f_source: Optional[str] = None
        val = data.get('source')
        if val is not None:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='source',
                    type='str',
                    name='Error',
                ))
            else:
                f_source = val
        f_message: Optional[str] = None
        val = data.get('message')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='message',
                name='Error',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='message',
                    type='str',
                    name='Error',
                ))
            else:
                f_message = val
        f_arguments: Optional[List[Arguments]] = None
        val = data.get('arguments')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='arguments',
                name='Error',
            ))
        else:
            f_arguments = []
            for item in val:
                parsed_arguments = Arguments.parse_data(item)
                if parsed_arguments.has_error:
                    errors.append(parsed_arguments.forward())
                else:
                    f_arguments.append(parsed_arguments.result)
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(Error(
            identifier=_not_none(f_identifier),
            source=f_source,
            message=_not_none(f_message),
            arguments=_not_none(f_arguments),
        ))

    def __repr__(self) -> str:
        return "Error(" + repr(self.export_data()) + ")"


class StartLauncherFailedEvent:
    """
    Report that the requested launcher could not be started.
    """
    __slots__ = ('identifier', 'error',)
    FULL_EVENT_NAME = 'petronia.core.api.foreman:start-launcher:failed'
    SHORT_EVENT_NAME = 'start-launcher:failed'

    def __init__(
        self,
        identifier: str,
        error: Error,
    ) -> None:
        self.identifier = identifier
        self.error = error

    @property
    def fully_qualified_event_name(self) -> str:  # pylint: disable=R0201
        """Get the full event name that this object encapsulates."""
        return StartLauncherFailedEvent.FULL_EVENT_NAME

    def export_data(self) -> Dict[str, Any]:  # pylint: disable=R0201
        """Create the event data structure, ready for marshalling."""
        ret: Dict[str, Any] = {
            'identifier': self.identifier,
            'error': self.error.export_data(),
        }
        return _strip_none(ret)

    @staticmethod
    def parse_data(data: Dict[str, Any]) -> StdRet['StartLauncherFailedEvent']:  # pylint: disable=R0912,R0911
        """Parse the marshalled data into this structured form.  This includes full validation."""
        errors: List[StdRet[None]] = []
        val: Any
        f_identifier: Optional[str] = None
        val = data.get('identifier')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='identifier',
                name='StartLauncherFailedEvent',
            ))
        else:
            if not isinstance(val, str):
                errors.append(StdRet.pass_errmsg(
                    _('Field {field_name} must be of type {type} for structure {name}'),
                    field_name='identifier',
                    type='str',
                    name='StartLauncherFailedEvent',
                ))
            else:
                f_identifier = val
        f_error: Optional[Error] = None
        val = data.get('error')
        if val is None:
            errors.append(StdRet.pass_errmsg(
                _('Required field {field_name} in {name}'),
                field_name='error',
                name='StartLauncherFailedEvent',
            ))
        else:
            parsed_error = Error.parse_data(val)
            if parsed_error.has_error:
                errors.append(parsed_error.forward())
            else:
                # Value, not result, because it could be optional...
                f_error = parsed_error.value
        if errors:
            return StdRet.pass_error(_not_none(collect_errors_from(errors)))
        return StdRet.pass_ok(StartLauncherFailedEvent(
            identifier=_not_none(f_identifier),
            error=_not_none(f_error),
        ))

    def __repr__(self) -> str:
        return "StartLauncherFailedEvent(" + repr(self.export_data()) + ")"


def _not_none(value: Optional[T]) -> T:
    assert value is not None
    return value


def _strip_none(dict_value: Dict[str, Any]) -> Dict[str, Any]:
    ret: Dict[str, Any] = {}
    for key, value in dict_value.items():
        if value is not None:
            ret[key] = value
    return ret
