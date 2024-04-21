from sqlalchemy.orm import Session

from schemas.boundaries import BoundariesCreate,BoundariesShow

from db.models.boundaries import Boundaries

from db.models.layer import Layer

def create_new_boundary(boundary_data: BoundariesCreate, db: Session):
    new_boundary = Boundaries(**boundary_data.dict())
    db.add(new_boundary)
    db.commit()
    db.refresh(new_boundary)
    return new_boundary


def get_boundaries(layer_id: int, db: Session):
    if layer_id > 0:
        return db.query(Boundaries, Layer)\
        .join(Layer, Boundaries.layer_id == Layer.id)\
        .filter(Boundaries.layer_id == layer_id)\
        .all()
    else:
        return db.query(Boundaries).all()
