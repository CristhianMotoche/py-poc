import types
from typing import Any, Literal, Self, Type, TypeVar, cast, reveal_type
from dataclasses import dataclass
import os
import typing

TV = TypeVar('TV')

@dataclass
class BaseConfig:

    @classmethod
    def load(cls) -> Self:
        th = typing.get_type_hints(cls, include_extras=True)
        c = cls(**{
            key: cls._load_env(key, type_hint)
            for key, type_hint in th.items()
        })
        return c

    @classmethod
    def _load_env(cls, key: str, type_to_apply: Type) -> Any:
        value = os.getenv(key)

        if not value:
            if None.__class__ not in typing.get_args(type_to_apply):
                raise ValueError("Missing env variables are not supported yet")
            return value
        else:
            remaining_types = list(filter(lambda arg: arg is not None.__class__, typing.get_args(type_to_apply)))
            if len(remaining_types) == 1:
                return cls._check_type(key, value, remaining_types[0])
            else:
                return cls._check_type(key, value, type_to_apply)

    @classmethod
    def _check_type(cls, key: str, value: str, type_to_apply: Type) -> Any:
        if isinstance(type_to_apply, types.UnionType):
            return cls._try_union_types(key, value, cast(types.UnionType, type_to_apply))
        elif issubclass(type_to_apply, bool):
            return value == "True"
        elif issubclass(type_to_apply, int):
            return int(value)
        elif issubclass(type_to_apply, float):
            return float(value)
        elif issubclass(type_to_apply, str):
            return value
        else:
            raise ValueError(f"The given type ({type_to_apply}) for {key} cannot be used to parse an env variable")

    @classmethod
    def _try_union_types(cls, key: str, value: str, type_to_apply: types.UnionType) -> Any:
        for inner_type_to_apply in typing.get_args(type_to_apply):
            try:
                return cls._check_type(key, value, inner_type_to_apply)
            except ValueError:
                continue
        raise ValueError(
            f'The value {value} is not of any of these types'
            f' {typing.get_args(type_to_apply)}'
        )
