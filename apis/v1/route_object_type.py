from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.object_type import ObjectTypeCreate,ShowObjectType
from db.session import get_db
from db.repository.object_type import create_object_type,retrieve_object_type
from db.models.object_type import Object_type
from typing import List

router = APIRouter()


@router.get("/first-type/", response_model=str, status_code=status.HTTP_200_OK)
def get_first_type(db: Session = Depends(get_db)):

    """ Получить первый тип объекта. """
    try:
        first_type = db.query(Object_type.type).distinct().order_by(Object_type.type).first()
        if first_type:
            return first_type[0]
        else:
            raise HTTPException(status_code=404, detail="Тип объекта не найден")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Не удалось получить данные о типе объекта: {e}")


@router.get("/second-type/", response_model=str, status_code=status.HTTP_200_OK)
def get_second_type(db: Session = Depends(get_db)):
    """ Получить второй тип объекта. """
    try:

        second_type = db.query(Object_type.type).distinct().order_by(Object_type.type).offset(1).first()
        if second_type:

            return second_type[0]
        else:
            raise HTTPException(status_code=404, detail="Тип объекта не найден")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Не удалось получить данные о типе объекта: {e}")


@router.get("/third-type/", response_model=str, status_code=status.HTTP_200_OK)
def get_third_type(db: Session = Depends(get_db)):
    """ Получить третий тип объекта. """
    try:

        third_type = db.query(Object_type.type).distinct().order_by(Object_type.type).offset(2).first()
        if third_type:

            return third_type[0]
        else:
            raise HTTPException(status_code=404, detail="Тип объекта не найден")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Не удалось получить данные о типе объекта: {e}")
