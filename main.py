from iterator import Iterator


class MyIter:
    def __init__(self, x: int) -> None:
        self.x = x


class Impl(Iterator, MyIter):
    Item = int

    def next(self):
        self.x += 1
        return self.x


iterator = MyIter(5)

for i in iterator:
    print(i)
    if i >= 50:
        break
