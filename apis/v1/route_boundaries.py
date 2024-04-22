from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.boundaries import BoundariesCreate, BoundariesShow
from db.repository.boundaries import create_new_boundary,get_boundaries
from db.session import get_db
from db.models.layer import Layer
from db.models.boundaries import Boundaries

router = APIRouter()

@router.post("/boundaries/", response_model=BoundariesShow, status_code=status.HTTP_201_CREATED)
def add_boundary(boundary_data: BoundariesCreate, db: Session = Depends(get_db)):
    try:
        new_boundary = create_new_boundary(boundary_data=boundary_data, db=db)
        return new_boundary
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при создании границы объекта: {e}")



@router.get("/boundaries/", response_model=List[BoundariesShow], status_code=status.HTTP_200_OK)
def read_boundaries(db: Session = Depends(get_db)):
    """
    Возвращает список всех границ.
    """
    boundaries = get_boundaries(db=db)
    return boundaries

# @router.get("/boundaries/with_layers", response_model=List[BoundariesWithLayerShow], status_code=status.HTTP_200_OK)
# def read_boundaries_with_layers(db: Session = Depends(get_db)):
#     """
#     Возвращает список всех границ с информацией о слоях.
#     """
#     boundaries = get_boundaries_with_layers(db=db)
#     return boundaries
#
# @router.get("/boundaries/{boundary_id}", response_model=BoundariesWithLayerShow)
# def get_boundary_with_layer(boundary_id: int, db: Session = Depends(get_db)):
#     boundary = db.query(Boundaries).join(Layer).filter(Boundaries.id == boundary_id).first()
#     if boundary is None:
#         raise HTTPException(status_code=404, detail="Граница не найдена")
#     return boundary