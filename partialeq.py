from typing import Generic, TypeVar

from trait import Trait, implemented


T = TypeVar("T")


class PartialEq(Trait, Generic[T]):
    """
    Trait for comparing equality
    """

    def eq(self, other: T) -> bool:
        ...

    @implemented
    def ne(self, other: T) -> bool:
        return not self.eq(other)


class Eq(Trait, Generic[T], super_traits=(PartialEq[T],)):
    """
    Trait for comparing equality
    """
