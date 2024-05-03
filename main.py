from fastapi import FastAPI

from models import Snowboard, CreateSnowboard
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
def create_snowboard(new_snowboard:CreateSnowboard) -> str:
    snowboard_id = len(snowboards)+1
    snowboard = Snowboard(
        id = snowboard_id,
        length = new_snowboard.length,
        color = new_snowboard.color,
        has_bindings = new_snowboard.has_bindings,
        brand = new_snowboard.brand)
    snowboards.append(snowboard)
    return "Snowboard added succesfully."


@app.put("/snowboards")
async def update_snowboard(updated_snowboard: Snowboard, snowboard_id: int = None):
    for i, snowboard in enumerate(snowboards):
        if snowboard_id == snowboard.id:
            snowboards[i] = updated_snowboard
            return "Snowboard updated successfully"
    create_snowboard(updated_snowboard)


@app.delete("/snowboards/{snowboard_id}")
async def delete_snowboard(snowboard_id: int) -> str:
    for i, snowboard in enumerate(snowboards):
        if snowboard_id == snowboard.id:
            snowboards.pop(i)
            return "Snowboard deleted"
        
