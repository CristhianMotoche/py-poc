import os
from typing import Literal
from pydantic import BaseModel

class Config(BaseModel):
    PORT: Literal['FOO', 'BAR']

conf = Config(**dict(os.environ.items()))

print(conf.PORT)
