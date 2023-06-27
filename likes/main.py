from typing import Literal
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from prisma import Prisma

app = FastAPI()

prisma = Prisma()


LikeType = Literal["food", "sports"]

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    await prisma.connect()
    response = await call_next(request)
    await prisma.disconnect()
    return response

class Like(BaseModel):
    id: int
    name: str
    type_: LikeType

class Person(BaseModel):
    id: int
    likes: list[Like]

@app.get("/persons")
async def all_person() -> list[Person]:
    users = await prisma.user.find_many()
    return list(map(lambda x: Person(id=x.id, likes=[]), users))

@app.get("/persons/{item_id}")
async def get_person(item_id: int) -> Person:
    userOp = await prisma.user.find_first(where={ 'id': item_id })
    if not userOp:
        raise HTTPException(status_code=404, detail="Person not found")
    return Person(id=userOp.id, likes=[])

@app.post("/persons")
async def add_persons(person: Person) -> Person:
    user = await prisma.user.create(
        data={ 'name': f'User #{person.id}' },
    )
    print('CL - user', user)
    return person
