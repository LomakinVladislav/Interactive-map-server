from pydantic import BaseModel


class ObjectCreate(BaseModel):
    address: str
    area: float
    cadastral_number: str
    redemption_cost: int
    redemption_period: str
    num_residents: int
    owner_ship_rights: str
    redemption_status_id: int


class ObjectShow(BaseModel):
    id: int
    address: str
    area: float
    cadastral_number: str
    redemption_cost: int
    redemption_period: str
    num_residents: int
    owner_ship_rights: str
    redemption_status_id: int

    class Config:
        orm_mode = True
