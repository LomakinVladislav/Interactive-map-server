from pydantic import BaseModel


class ObjectTypeCreate(BaseModel):
    type: str

class ShowObjectType(ObjectTypeCreate):
    id: int


    class Config():
        orm_mode =True
