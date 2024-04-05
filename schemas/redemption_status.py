from pydantic import BaseModel


class RedemptionStatusCreate(BaseModel):
    status_name: str

class ShowStatus(RedemptionStatusCreate):
    id:int


    class Config():
        orm_mode =True

