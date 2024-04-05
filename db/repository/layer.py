from sqlalchemy.orm import Session

from schemas.layer import LayerCreate
from db.models.layer import Layer

def create_new_layer(layer_data: LayerCreate, db: Session):
    new_layer = Layer(**layer_data.dict())
    db.add(new_layer)
    db.commit()
    db.refresh(new_layer)
    return new_layer
