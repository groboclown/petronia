from typing import Optional, Iterable, Union, Mapping, Any, Callable


class Renderer:
    def __init__(
            self,
            file_encoding: Optional[str] = None,
            string_encoding: Optional[str] = None,
            decode_errors: Optional[str] = None,
            search_dirs: Optional[Iterable[str]] = None,
            file_extension: Union[None, bool, str] = None,
            escape: Optional[Callable[[str], str]] = None,
            partials: Optional[Mapping[str, Any]] = None,
            missing_tags: Optional[str] = None,
    ) -> None: ...

    def render(
            self,
            template: str,
            *context: Mapping[str, Any],
            **kwargs: Any,
    ) -> str: ...
