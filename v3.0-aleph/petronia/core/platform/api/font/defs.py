
"""
Definitions for fonts.
"""


class FontDefinition:
    """
    The details for a font installed in the platform.
    """
    __slots__ = (
        '__family', '__name', '__category', '__quality',
        '__min_size', '__max_size',
    )

    def __init__(
            self,
            family: str,
            name: str,
            category: str,
            quality: int,
            min_size: int,
            max_size: int
    ) -> None:
        self.__family = family
        self.__name = name
        self.__category = category
        self.__quality = quality
        self.__min_size = min_size
        self.__max_size = max_size
