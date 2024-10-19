from decimal import Decimal
from fastapi import FastAPI
from pydantic import BaseModel, Field


class FuelModel(BaseModel):
    gas: Decimal = Field(alias="gas(euro/MWh)")
    kerosine: Decimal = Field(alias="kerosine(euro/MWh)")
    co2: Decimal = Field(alias="co2(euro/ton)")
    wind: Decimal = Field(alias="wind(%)")


class PowerplantsModel(BaseModel):
    name: str
    type: str
    efficiency: Decimal = Field(le=1, gt=0)
    pmin: Decimal
    pmax: Decimal


class Payload(BaseModel):
    load: int
    fuels: FuelModel
    powerplants: list[PowerplantsModel]


class Response(BaseModel):
    name: str
    p: Decimal


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/productionplan")
def productionplan(payload: Payload) -> list[Response]:
    print(payload)
    return [{"name": "windpark1", "p": 90.0}, {"name": "windpark2", "p": 21.6}]
