from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


LikeType = Literal["food", "sports"]

class Like(BaseModel):
    id: int
    name: str
    type_: LikeType

class Person(BaseModel):
    id: int
    likes: list[Like]

@app.get("/persons/{item_id}")
def read_persons(item_id: int) -> Person:
    return Person(id=item_id, likes=[Like(id=1, name="Pineable", type_="food")])

@app.post("/persons")
def add_persons(person: Person) -> Person:
    return person
