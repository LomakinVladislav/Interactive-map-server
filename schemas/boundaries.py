from pydantic import BaseModel


class BoundariesCreate(BaseModel):
    object_id: int
    layer_id: int
    latitude: float
    longitude: float


class BoundariesShow(BaseModel):
    id: int
    object_id: int
    layer_id: int
    latitude: float
    longitude: float




    class Config:
        orm_mode = True

