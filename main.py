from fastapi import FastAPI

from models import Snowboard
import json


app = FastAPI()

with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

snowboards: list[Snowboard] = []

for snowboard in snowboard_list:
    snowboards.append(Snowboard(**snowboard))

@app.get("/snowboards")
async def get_snowboards() -> list[Snowboard]:
    return snowboards

@app.post("/snowboards")
def create_snowboard(snowboard: Snowboard) -> None:
    snowboards.append(snowboard)

@app.put("/snowboards/{snowboard_id}")
async def update_snowboard(snowboard_id: int, updated_snowboard: Snowboard) -> str:
    for snowboard in range(len(snowboards)):
        if snowboard_id == snowboards[snowboard].id:
            snowboards[snowboard] = updated_snowboard
            return "Snowboard updated successfully"

@app.delete("/snowboards/{snowboard_id}")
async def delete_snowboard(snowboard_id: int) -> str:
    for i, snowboard in enumerate(snowboards):
        if snowboard_id == snowboard.id:
            snowboards.pop(i)
            return "Snowboard deleted"
