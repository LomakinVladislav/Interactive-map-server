from fastapi import APIRouter,HTTPException,status
from sqlalchemy.orm import Session
from fastapi import Depends
from  schemas.object import ObjectCreate,ObjectShow
from db.session import get_db
from db.repository.object import create_new_object

router = APIRouter()


@router.post("/objects/", response_model=ObjectShow, status_code=status.HTTP_201_CREATED)
def add_object(object_data: ObjectCreate, db: Session = Depends(get_db)):
    try:
        new_object = create_new_object(object_data=object_data, db=db)
        return new_object
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при создании объекта: {e}")