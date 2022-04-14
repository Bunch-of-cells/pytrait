# Traits in Python

## Create a new trait
```
from trait import Trait, implemented

class MyTrait(Trait):
    def my_func(pass):
        ...

    @implemented
    def default(self):
        print("This is the default implementation")

    def _personal_method(self):
        print("This is a personal method, cannot be accessed by anyone")

```

## How Impl a Trait
```
class MyClass:
    pass

class Impl(MyTrait, MyClass):
    def my_func(self):
        print("This is the implementation of my_func")
```