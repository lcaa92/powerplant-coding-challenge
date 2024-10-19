from typing import Union
from decimal import Decimal
from fastapi import FastAPI
from pydantic import BaseModel


class Payload(BaseModel):
    load: int
    fuels: object
    powerplants: object


class Response(BaseModel):
    name: str
    p: Decimal


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/productionplan")
def productionplan(payload: Payload) -> list[Response]:
    print(payload)
    return [{"name": "windpark1", "p": 90.0}, {"name": "windpark2", "p": 21.6}]
