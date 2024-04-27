from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.object import ObjectShow
from db.session import get_db
from db.models.object import Object
from typing import List,Optional

router = APIRouter()

@router.get("/objects/", response_model=List[ObjectShow], status_code=status.HTTP_200_OK)
def read_objects(object_type_id: Optional[int] = None, db: Session = Depends(get_db)):
    """
    Получить список объектов по типу объекта
    """
    query = db.query(Object)

    if object_type_id is not None:
        objects = query.filter(Object.object_type_id == object_type_id).all()
        if not objects:
            raise HTTPException(status_code=404, detail="Объекты с данным типом не найдены")
    else:
        objects = query.all()
        if not objects:
            raise HTTPException(status_code=404, detail="Объекты не найдены")

    return objects