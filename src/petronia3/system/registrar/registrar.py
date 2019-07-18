
# mypy: allow-any-explicit
# mypy: allow-any-expr

"""
The registrar class itself.
"""

from typing import Dict, Type, Tuple, Optional, Any
from .registrar_types import CategoryFactory
from ..participant import ComponentId
from ...util.memory import T
from ...validation import assert_formatted


class Registrar:
    """
    Simple category registrar handler.
    """
    __slots__ = ('_categories',)
    _categories: Dict[str, Tuple[Type[Any], CategoryFactory[Any]]]

    def __init__(self) -> None:
        self._categories = {}

    def register_category(
            self, category: str,
            construction_type: Type[T],
            factory: CategoryFactory[T]
    ) -> None:
        assert_formatted(
            category not in self._categories,
            'Registrar',
            'category registration',
            'category {0} already registered',
            category
        )
        self._categories[category] = (construction_type, factory,)

    def create_new_category_instance(
            self, category: str,
            construction_obj: T
    ) -> Optional[ComponentId]:
        if category in self._categories:
            ctty, factory = self._categories[category]
            assert_formatted(
                isinstance(construction_obj, ctty),
                'Registrar',
                'category creation',
                'category {0} requires objects of type {1}, found {2}',
                category, ctty, construction_obj
            )
            return factory(construction_obj)
        else:
            return None
