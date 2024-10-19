
from fastapi import FastAPI
from models import Payload, Response

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/productionplan")
def productionplan(payload: Payload) -> list[Response]:
    print(payload)
    return [{"name": "windpark1", "p": 90.0}, {"name": "windpark2", "p": 21.6}]
