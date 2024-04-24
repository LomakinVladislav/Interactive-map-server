from sqlalchemy.orm import Session
from db.models.object_type import Object_type
from schemas.object_type import ObjectTypeCreate

def create_object_type(city_and_project_data: ObjectTypeCreate, db: Session):
    object_type = ObjectTypeCreate(**city_and_project_data.dict())
    db.add(object_type)
    db.commit()
    db.refresh(object_type)
    return object_type

def retrieve_object_type(db: Session, object_type_id: int):
    return db.query(Object_type).filter(Object_type.id == object_type_id).first()
