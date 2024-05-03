from sqlalchemy.orm import Session
from schemas.object import ObjectCreate
from db.models.object import Object


def create_new_object(object_data: ObjectCreate, db: Session):
    new_object = Object(**object_data.dict()
    )
    db.add(new_object)
    db.commit()
    db.refresh(new_object)
    return new_object

def retrieve_object(db: Session, object_id: int):
    return db.query(Object).filter(Object.id == object_id).first()
def retrieve_all_objects(db: Session):
    return db.query(Object).all()




