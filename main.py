
from fastapi import FastAPI
from models import Payload, Response
from power_calculator import PowerCalculator

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/productionplan")
def productionplan(payload: Payload) -> list[Response]:
    print(payload)

    service = PowerCalculator(
        load=payload.load,
        fuels=payload.fuels,
        powerplants=payload.powerplants
    )
    return service.get_powerplants_power()
