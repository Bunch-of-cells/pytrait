from typing_extensions import TypeAlias
from trait import Trait, private_impl


class Iterator(Trait):
    Item: TypeAlias = None

    def next(self) -> Item:
        ...

    @private_impl
    def __iter__(self):
        return self

    @private_impl
    def __next__(self) -> Item:
        return self.next()
