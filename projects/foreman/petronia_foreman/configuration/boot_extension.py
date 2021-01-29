"""An extension-like metadata file for boot-time extensions."""

from typing import Iterable, Sequence, Mapping, Tuple, Optional, Any
import json
from petronia_common.extension.config import ExtensionVersion
from petronia_common.util import readonly_dict
from ..events import foreman


class BootExtensionMetadata:  # pylint:disable=too-many-instance-attributes
    """
    Contains all the data necessary to start up the extension using a standard registered
    runtime.  This simulates the data passed from the extension-loader events.
    """

    __slots__ = (
        '__name', '__version', '__runtime', '__locations',
        '__produces', '__consumes',
        '__permissions', '__configuration',
    )

    def __init__(  # pylint: disable=too-many-arguments
            self,
            name: str,
            version: ExtensionVersion,
            runtime: str,
            produces: Iterable[str],
            consumes: Iterable[Tuple[Optional[str], Optional[str]]],
            permissions: Mapping[str, Iterable[str]],
            configuration: Mapping[str, Any],
            locations: Iterable[str],
    ) -> None:
        self.__name = name
        self.__version = version
        self.__runtime = runtime
        self.__produces = tuple(produces)
        self.__consumes = tuple(consumes)
        self.__permissions: Mapping[str, Sequence[str]] = readonly_dict({
            key: tuple(value)
            for key, value in permissions.items()
        })
        self.__configuration = configuration
        self.__locations = tuple(locations)

    @property
    def consumes(self) -> Iterable[Tuple[Optional[str], Optional[str]]]:
        """Return a list of event-id, target-id tuples that this extension
        listens to out-of-the-gate."""
        return self.__consumes

    def to_start_event(self) -> foreman.LauncherStartExtensionRequestEvent:
        """Convert this object into an extension start request."""
        return foreman.LauncherStartExtensionRequestEvent(
            name=self.__name,
            version=list(self.__version),
            location=list(self.__locations),
            runtime=self.__runtime,
            send_access=list(self.__produces),
            configuration=json.dumps(self.__configuration),
            permissions=[
                foreman.ExtensionPermission(action, list(resources))
                for action, resources in self.__permissions.items()
            ],
        )
