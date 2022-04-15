from typing import Generic, TypeVar

from trait import Trait, implemented, private_impl


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

    @private_impl
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, T):
            return NotImplemented
        return self.eq(__o)

    @private_impl
    def __ne__(self, __o: object) -> bool:
        if not isinstance(__o, T):
            return NotImplemented
        return self.ne(__o)


T_EQ = TypeVar("T_EQ", bound="Eq")


class Eq(Trait, super_traits=(PartialEq[T_EQ],)):
    """
    Trait for comparing equality
    """
