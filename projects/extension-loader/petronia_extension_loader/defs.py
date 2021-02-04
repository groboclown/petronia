"""Simple definition types."""

from typing import Sequence, Set
from petronia_common.extension.config import AbcExtensionMetadata, ExtensionVersion

TRANSLATION_CATALOG = 'extension-loader'


class ExtensionInfo:
    """Information about an extension.  Extensions must be installed to the data path."""
    __slots__ = ('__path', '__metadata', '__origin_ids')

    def __init__(
            self,
            path: Sequence[str], metadata: AbcExtensionMetadata,
    ) -> None:
        self.__path = tuple(path)
        self.__metadata = metadata
        self.__origin_ids: Set[str] = set()

    @property
    def path(self) -> Sequence[str]:
        """Path that allows for loading the extension."""
        return self.__path

    @property
    def metadata(self) -> AbcExtensionMetadata:
        """Extension metadata information."""
        return self.__metadata

    @property
    def name(self) -> str:
        """The extension name."""
        return self.__metadata.name

    @property
    def version(self) -> ExtensionVersion:
        """The extension version."""
        return self.__metadata.version

    @property
    def request_source_ids(self) -> Sequence[str]:
        """All origin source IDs that requested this extension to load."""
        return tuple(self.__origin_ids)

    def add_request_source_id(self, *source_id: str) -> None:
        """Add a source-id that requested this extension to load."""
        self.__origin_ids.update(source_id)
