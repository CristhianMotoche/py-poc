import types
from typing import Any, Literal, Self, Type, TypeVar, cast, reveal_type
from dataclasses import dataclass
import os
import typing

TV = TypeVar('TV')

@dataclass
class Config:
    PORT: int
    HOSTNAME: str
    # ENV: Literal["prod", "dev"]

    @classmethod
    def load(cls) -> Self:
        th = typing.get_type_hints(cls)
        c = cls(**{
            key: cls._load_env(key, type_hint)
            for key, type_hint in th.items()
        })
        print("C", c)
        return c

    @classmethod
    def _load_env(cls, key: str, type_to_apply: Type[TV]) -> TV:
        value = os.getenv(key)

        if not value:
            raise ValueError("Missing env variables are not supported yet")

        match type_to_apply.__name__:
            case 'int':
                return type_to_apply(value)
            case 'str':
                return type_to_apply(value)
            case 'UnionType':
                return cls._try_union_types(value, cast(types.UnionType, type_to_apply))
            case x:
                raise ValueError(f"The given type ({x}) cannot be used to parse an env variable")

        # if value and not isinstance(type_to_apply, types.UnionType):
        #     return type_to_apply(value)

        # elif value and isinstance(type_to_apply, types.UnionType):
        #     return cls._try_union_types(value, type_to_apply)

        # raise ValueError()

    @classmethod
    def _try_union_types(cls, value: str, type_to_apply: types.UnionType) -> Any:
        for inner_type_to_apply in type_to_apply.__args__:
            try:
                return inner_type_to_apply(value)
            except ValueError:
                continue
        raise ValueError(
            f'The value {value} is not of any of these types'
            f' {type_to_apply.__args__}'
        )

try:
    config = Config.load()
    reveal_type(config.PORT)
except ValueError as ve:
    print(ve)
