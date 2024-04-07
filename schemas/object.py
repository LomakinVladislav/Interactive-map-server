from pydantic import BaseModel
from typing import Optional

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

class ObjectUpdate(BaseModel):
    address: Optional[str] = None
    area: Optional[float] = None
    cadastral_number: Optional[str] = None
    redemption_cost: Optional[int] = None
    redemption_period: Optional[str] = None
    num_residents: Optional[int] = None
    owner_ship_rights: Optional[str] = None


    class Config:
        orm_mode = True
