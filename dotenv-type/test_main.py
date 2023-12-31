import os
from typing import Literal
from unittest import TestCase, main
from main import BaseConfig
from dataclasses import dataclass


@dataclass
class Config(BaseConfig):
    PORT: int
    HOSTNAME: str
    TRESHOLD: float
    IS_SECURE: bool
    UNION: int | bool


class ConfigHappyPathTest(TestCase):
    def setUp(self):
        os.environ["PORT"] = "8080"
        os.environ["HOSTNAME"] = "8080"
        os.environ["TRESHOLD"] = "3.1415"
        os.environ["IS_SECURE"] = "True"
        os.environ["UNION"] = "True"

    def test_parses_int(self):
        config = Config.load()
        assert config.PORT == 8080
        assert type(config.PORT) == int

    def test_parses_float(self):
        config = Config.load()
        assert type(config.TRESHOLD) == float

    def test_parses_bool_true(self):
        config = Config.load()
        assert config.IS_SECURE == True

    def test_parses_bool_false(self):
        os.environ["IS_SECURE"] = "False"
        config = Config.load()
        assert config.IS_SECURE == False

    def test_parses_union_left(self):
        os.environ["UNION"] = "123"
        config = Config.load()
        assert config.UNION == 123

    def test_parses_union_right(self):
        os.environ["UNION"] = "True"
        config = Config.load()
        assert config.UNION == True


@dataclass
class UnhappyOne(BaseConfig):
    One: int


@dataclass
class UnhappyTwo(BaseConfig):
    ENV: Literal["prod", "dev"]


class ConfigUnhappyPathTest(TestCase):
    def setUp(self):
        os.environ["ONE"] = "ABC"

    def test_returns_value_error_on_wrong_type(self):
        with self.assertRaises(ValueError):
            UnhappyOne.load()

    def test_returns_value_error_on_literal_types_because_of_missing_support(self):
        with self.assertRaises(ValueError):
            UnhappyTwo.load()

if __name__ == "__main__":
    main()
