import types
from typing import Any, Literal, Self
from dataclasses import dataclass
import os
import typing


@dataclass
class Config:
    PORT: int
    HOSTNAME: int | str
    ENV: Literal["prod", "dev"]

    @classmethod
    def load(cls) -> Self | None:
        th = typing.get_type_hints(cls)
        try:
            return cls(**{
                key: cls._load_env(key, value)
                for key, value in th.items()
            })
        except ValueError as ve:
            print(ve)
            return None

    @classmethod
    def _load_env(cls, key: str, type_to_apply: Any) -> Any:
        value = os.getenv(key)
        print('Value', value)

        if value and not isinstance(type_to_apply, types.UnionType):
            return type_to_apply(value)

        elif value and isinstance(type_to_apply, types.UnionType):
            return cls._try_union_types(value, type_to_apply)

    @classmethod
    def _try_union_types(cls, value: str, type_to_apply: Any) -> Any:
        for inner_type_to_apply in type_to_apply.__args__:
            print('CL - inner_type_to_apply', inner_type_to_apply);
            try:
                return inner_type_to_apply(value)
            except ValueError:
                continue
        raise ValueError(f'The value {value} is not of any of these types {type_to_apply.__args__}')

config = Config.load()
print('CL - config', config);
