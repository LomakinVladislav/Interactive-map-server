from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from schemas.boundaries import BoundariesCreate, BoundariesShow
from db.repository.boundaries import create_new_boundary
from db.session import get_db

router = APIRouter()

@router.post("/boundaries/", response_model=BoundariesShow, status_code=status.HTTP_201_CREATED)
def add_boundary(boundary_data: BoundariesCreate, db: Session = Depends(get_db)):
    try:
        new_boundary = create_new_boundary(boundary_data=boundary_data, db=db)
        return new_boundary
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при создании границы объекта: {e}")