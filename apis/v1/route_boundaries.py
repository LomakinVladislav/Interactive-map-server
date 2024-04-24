from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from db.models.object import Object
from schemas.boundaries import BoundariesCreate, BoundariesShow
from db.models.object_type import Object_type
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


@router.get("/boundaries/first_object_type/", response_model=List[BoundariesShow], status_code=status.HTTP_200_OK)
def read_boundaries_by_first_object_type(db: Session = Depends(get_db)):
    """Возвращает координаты по первому типу объекта."""
    try:
        # получаем ID первого типа объекта
        first_object_type_id = db.query(Object_type).order_by(Object_type.id).first().id

        # получаем все границы, соответствующие этому типу объекта
        boundaries = (
            db.query(Boundaries)
            .join(Object)  # соединяем границы с объектами
            .filter(Object.object_type_id == first_object_type_id)  # Фильтруем объекты с первым типом
            .all()
        )
        if not boundaries:
            raise HTTPException(status_code=404, detail="Границы для данного типа объекта не найдены")
        return boundaries
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Ошибка при получении границ: {str(e)}")


@router.get("/boundaries/second_object_type/", response_model=List[BoundariesShow], status_code=status.HTTP_200_OK)
def read_boundaries_by_second_object_type(db: Session = Depends(get_db)):
    """Возвращает координаты по второму типу объекта."""
    try:
        # получаем второй тип объекта по ID
        second_object_type = db.query(Object_type).order_by(Object_type.id).offset(1).first()
        if not second_object_type:
            raise HTTPException(status_code=404, detail="Тип объекта не найден")

        # получаем все границы для объектов этого типа
        boundaries = (
            db.query(Boundaries)
            .join(Object)
            .filter(Object.object_type_id == second_object_type.id)
            .all()
        )
        if not boundaries:
            raise HTTPException(status_code=404, detail="Границы для данного типа объекта не найдены")
        return boundaries
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при запросе границ: {str(e)}")


@router.get("/boundaries/third_object_type/", response_model=List[BoundariesShow], status_code=status.HTTP_200_OK)
def read_boundaries_by_third_object_type(db: Session = Depends(get_db)):
    """Возвращает координаты по третьему типу объекта."""
    try:
        # получаем третий тип объекта по ID
        third_object_type = db.query(Object_type).order_by(Object_type.id).offset(2).first()
        if not third_object_type:
            raise HTTPException(status_code=404, detail="Тип объекта не найден")

        # получаем все границы для объектов этого типа
        boundaries = (
            db.query(Boundaries)
            .join(Object)
            .filter(Object.object_type_id == third_object_type.id)
            .all()
        )
        if not boundaries:
            raise HTTPException(status_code=404, detail="Границы для данного типа объекта не найдены")
        return boundaries

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при запросе границ: {str(e)}")
