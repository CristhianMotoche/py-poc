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


class ConfigHappyPathTest(TestCase):
    def setUp(self):
        pass

    def test_accepts_optional(self):
        config = Config.load()
        assert config.OPTIONAL is None

    def test_accepts_None_in_union_type(self):
        config = ConfigTwo.load()
        assert config.NONE_IN_UNION is None

if __name__ == "__main__":
    main()
