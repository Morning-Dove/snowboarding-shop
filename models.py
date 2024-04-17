from pydantic import BaseModel
from enum import Enum


class Brand(Enum):
    SALOMAN = "Saloman"
    NITRO = "Nitro"
    BURTON = "Burton"

class Snowboard(BaseModel):
    id: int
    length: int
    color: str
    has_bindings: bool
    brand: Brand


