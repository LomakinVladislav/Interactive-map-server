from sqlalchemy.orm import Session

from schemas.boundaries import BoundariesCreate,BoundariesShow

from db.models.boundaries import Boundaries

def create_new_boundary(boundary_data: BoundariesCreate, db: Session):
    new_boundary = Boundaries(**boundary_data.dict())
    db.add(new_boundary)
    db.commit()
    db.refresh(new_boundary)
    return new_boundary


def get_boundaries(db: Session):
    return db.query(Boundaries).all()


