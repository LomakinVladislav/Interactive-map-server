from pydantic import BaseModel

class LayerCreate(BaseModel):
    color: str
    description: str

class LayerShow(BaseModel):
    id: int
    color: str
    description: str


    class Config:
        orm_mode = True
