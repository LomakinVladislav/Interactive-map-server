from pydantic import BaseModel
from typing import Optional


class ObjectBase(BaseModel):
    class Config:
        orm_mode = True

class ObjectCreate(ObjectBase):
    address: str
    area: float
    cadastral_number: str
    redemption_cost: int
    redemption_period: str
    num_residents: int
    owner_ship_rights: str
    redemption_status_id: int


class ObjectShow(ObjectBase):
    id: int
    address: str
    area: float
    cadastral_number: str
    redemption_cost: int
    redemption_period: str
    num_residents: int
    owner_ship_rights: str
    redemption_status_id: int

class ObjectUpdate(ObjectBase):
    address: Optional[str] = None
    area: Optional[float] = None
    cadastral_number: Optional[str] = None
    redemption_cost: Optional[int] = None
    redemption_period: Optional[str] = None
    num_residents: Optional[int] = None
    owner_ship_rights: Optional[str] = None


