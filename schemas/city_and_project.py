from pydantic import BaseModel


class CityAndProjectCreate(BaseModel):
    city: str
    project_name: str

class ShowStatus(CityAndProjectCreate):
    id:int


    class Config():
        orm_mode =True

