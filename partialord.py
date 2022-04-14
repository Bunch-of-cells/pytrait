from enum import Enum, auto
from typing import Generic, TypeVar
from trait import Trait

T = TypeVar("T")


class Ordering(Enum):
    LesserThan = auto()
    Equal = auto()
    GreaterThan = auto()


class PartialOrd(Trait, Generic[T]):
    """
    Trait for comparing
    """

    def partial_cmp(self, other: T) -> Ordering:
        ...


class Ord(Trait, Generic[T], super_traits=(PartialOrd[T],)):
    """
    Trait for comparing
    """

    def cmp(self, other: T) -> Ordering:
        ...
