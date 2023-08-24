import os
from typing import Optional
from unittest import TestCase, main
from main import BaseConfig
from dataclasses import dataclass


@dataclass
class Config(BaseConfig):
    OPTIONAL: Optional[int]

@dataclass
class ConfigTwo(BaseConfig):
    NONE_IN_UNION: str | None


@dataclass
class UnhappyOne(BaseConfig):
    NONE_IN_UNION: int | None


class ConfigOptionalTest(TestCase):
    def setUp(self):
        pass

    def test_accepts_optional(self):
        config = Config.load()
        assert config.OPTIONAL is None

    def test_accepts_None_in_union_type(self):
        config = ConfigTwo.load()
        assert config.NONE_IN_UNION is None

    def test_parses_not_none(self):
        os.environ["OPTIONAL"] = "123"
        config = Config.load()
        assert config.OPTIONAL == 123

    def test_returns_value_error_on_wrong_type_not_none(self):
        os.environ["NONE_IN_UNION"] = "FOOBAR"
        with self.assertRaises(ValueError):
            UnhappyOne.load()

if __name__ == "__main__":
    main()
