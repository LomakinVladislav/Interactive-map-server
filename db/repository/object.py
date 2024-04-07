from sqlalchemy.orm import Session
from schemas.object import ObjectCreate
from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import date
from db.models.object import Object


def create_new_object(object_data: ObjectCreate, db: Session):
    new_object = Object(
        address=object_data.address,
        area=object_data.area,
        cadastral_number=object_data.cadastral_number,
        redemption_cost=object_data.redemption_cost,
        redemption_period=object_data.redemption_period,
        num_residents=object_data.num_residents,
        owner_ship_rights=object_data.owner_ship_rights,
        redemption_status_id=object_data.redemption_status_id
    )
    db.add(new_object)
    db.commit()
    db.refresh(new_object)
    return new_object



class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: date

def retrieve_all_objects(db: Session):
    return db.query(Object).all()

def retrieve_object(db: Session, object_id: int):
    return db.query(Object).filter(Object.id == object_id).first()



    class Config():
        orm_mode = True



