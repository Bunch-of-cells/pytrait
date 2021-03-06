from collections.abc import Callable
from typing import Any, Literal, Protocol, TypeVar, overload


class TraitMeta(type):
    @overload
    def __new__(
        mcls,
        name: Literal["Impl"],
        bases: tuple[type, type],
        namespace: dict[str, Any],
        /,
        super_traits: tuple[type, ...] = (),
        **kwargs: Any,
    ) -> None:
        ...

    @overload
    def __new__(
        mcls,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        /,
        super_traits: tuple[type, ...] = (),
        **kwargs: Any,
    ):
        ...

    def __new__(
        mcls,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        /,
        super_traits: tuple[type, ...] = (),
        **kwargs: Any,
    ):
        if name == "Impl":
            if len(bases) != 2:
                raise ValueError("Impl must have exactly two bases")
            trait, cls = bases
            if "__trait__" not in vars(trait):
                raise ValueError("First base of Impl must be a trait")
            if "__trait__" in vars(cls):
                raise ValueError("Cannot Impl on a trait")

            required = vars(trait)["__super_traits__"]
            impls = vars(cls).get("__impls__", ())
            for t in required:
                t = getattr(t, "__origin__", t)
                if t not in impls:
                    raise ValueError(
                        f"{t.__name__} is not implemented for {cls.__name__}, which is required in order for the implementation of {trait.__name__}"
                    )

            unimplemented = {
                k: v for k, v in vars(trait).items() if not k.startswith("_")
            }

            private = {
                k: v for k, v in vars(trait).items() if hasattr(v, "private_impl")
            }

            for k, v in namespace.items():
                if k.startswith("_"):
                    continue
                if k in unimplemented:
                    setattr(cls, k, v)
                    del unimplemented[k]
                    continue
                raise ValueError(f"'{k}' is not a trait method for {trait.__name__}")

            for method, value in unimplemented.items():
                if not hasattr(value, "implemented"):
                    raise ValueError(
                        f"method '{method}' of trait {trait.__name__} is not implemented"
                    )
                else:
                    setattr(cls, method, value)

            for method, value in private.items():
                setattr(cls, method, value)

            impls = getattr(cls, "__impls__", [])
            impls.append(trait)
            return setattr(cls, "__impls__", impls)

        if bases and Trait in bases:
            namespace["__trait__"] = True
            namespace["__super_traits__"] = super_traits

        __import__(namespace["__module__"]).__dict__[f"{name}Item"] = super().__call__(
            type(Protocol), f"{name}Item", (Protocol,), namespace
        )
        return super().__new__(mcls, name, bases, namespace, **kwargs)

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if "__trait__" in vars(cls):
            raise TypeError("Cannot instantiate a trait")
        return super().__call__(*args, **kwargs)


class Trait(metaclass=TraitMeta):
    pass


T = TypeVar("T", bound=Callable)


def implemented(method: T) -> T:
    setattr(method, "implemented", True)
    return method


def private_impl(method: T) -> T:
    setattr(method, "private_impl", True)
    return method
