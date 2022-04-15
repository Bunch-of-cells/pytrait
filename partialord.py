from enum import Enum, auto
from typing import Generic, TypeVar

from trait import Trait, private_impl

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

    @private_impl
    def __le__(self, other: object) -> bool:
        if not isinstance(other, T):
            return NotImplemented
        return self.partial_cmp(other) in (Ordering.LesserThan, Ordering.Equal)

    @private_impl
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, T):
            return NotImplemented
        return self.partial_cmp(other) == Ordering.LesserThan

    @private_impl
    def __ge__(self, other: object) -> bool:
        if not isinstance(other, T):
            return NotImplemented
        return self.partial_cmp(other) in (Ordering.GreaterThan, Ordering.Equal)

    @private_impl
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, T):
            return NotImplemented
        return self.partial_cmp(other) == Ordering.GreaterThan


T_ORD = TypeVar("T_ORD", bound="Ord")


class Ord(Trait, super_traits=(PartialOrd[T_ORD],)):
    """
    Trait for comparing
    """

    def cmp(self, other: T_ORD) -> Ordering:
        ...
