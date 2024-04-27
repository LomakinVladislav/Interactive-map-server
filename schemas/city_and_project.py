from pydantic import BaseModel


class CityAndProjectCreate(BaseModel):
    city: str
    project_name: str


class CityAndProjectShow(BaseModel):
    city: str
    project_name: str

class ShowProject(CityAndProjectCreate):
    id:int

class ProjectName(BaseModel):
    project_name: str

class City(BaseModel):
    city: str

    class Config():
        orm_mode =True

