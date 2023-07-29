import os
from unittest import TestCase, main
from main import BaseConfig
from dataclasses import dataclass


@dataclass
class Config(BaseConfig):
    PORT: int
    HOSTNAME: str
    TRESHOLD: float
    IS_SECURE: bool
    # ENV: Literal["prod", "dev"]


class ConfigHappyPathTest(TestCase):
    def setUp(self):
        os.environ["PORT"] = "8080"
        os.environ["HOSTNAME"] = "8080"
        os.environ["TRESHOLD"] = "3.1415"
        os.environ["IS_SECURE"] = "True"

    def test_parses_int(self):
        config = Config.load()
        assert config.PORT == 8080
        assert type(config.PORT) == int

if __name__ == "__main__":
    main()
