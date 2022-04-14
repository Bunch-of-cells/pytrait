from partialeq import PartialEq, Eq, EqItem
from partialord import Ord, Ordering, PartialOrd, OrdItem


class MyInt:
    def __init__(self, x: int) -> None:
        self.x = x


class Impl(PartialEq[MyInt], MyInt):
    def eq(self, other: MyInt) -> bool:
        return self.x == other.x


class Impl(Eq[MyInt], MyInt):
    pass


class Impl(PartialOrd[MyInt], MyInt):
    def partial_cmp(self, other: MyInt) -> Ordering:
        if self.x < other.x:
            return Ordering.LesserThan
        elif self.x > other.x:
            return Ordering.GreaterThan
        else:
            return Ordering.Equal


class Impl(Ord[MyInt], MyInt):
    def cmp(self, other: MyInt) -> Ordering:
        if self.x < other.x:
            return Ordering.LesserThan
        elif self.x > other.x:
            return Ordering.GreaterThan
        else:
            return Ordering.Equal


def is_equal(first: EqItem, second: EqItem):
    print(first.eq(second))


def is_equal_ord(first: OrdItem, second: OrdItem):
    print(first.partial_cmp(second) == Ordering.Equal)


no1 = MyInt(4)
no2 = MyInt(5)
is_equal(no1, no2)
is_equal_ord(no1, no2)
