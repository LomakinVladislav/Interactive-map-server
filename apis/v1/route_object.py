from fastapi import APIRouter,HTTPException,status
from sqlalchemy.orm import Session
from fastapi import Depends
from  schemas.object import ObjectCreate,ObjectShow,ObjectUpdate
from db.session import get_db
from db.repository.object import create_new_object,retrieve_object,retrieve_all_objects
from typing import List
from fastapi import Body
from db.models.object import Object



router = APIRouter()


@router.post("/objects/", response_model=ObjectShow, status_code=status.HTTP_201_CREATED)
async def create_object(object_data: ObjectCreate, db: Session = Depends(get_db)):
    """
    Создать новый объект.
    """
    try:
        new_object = create_new_object(object_data=object_data, db=db)
        return new_object
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при создании объекта: {e}")

@router.get("/object/{object_id}", response_model=ObjectShow, status_code=status.HTTP_200_OK)
def get_object(object_id: int, db: Session = Depends(get_db)):
    """
      Получить информацию об объекте по его ID.
      """
    object_item = retrieve_object(db=db, object_id=object_id)
    if object_item is None:
        raise HTTPException(status_code=404, detail="Объект не найден.")
    return object_item

@router.get("/objects/", response_model=List[ObjectShow], status_code=status.HTTP_200_OK)
def get_all_objects(db: Session = Depends(get_db)):
    """
    Возвращает список всех объектов недвижимости с их параметрами и статусами.
    """
    objects = retrieve_all_objects(db=db)
    return objects


@router.patch("/objects/{object_id}", response_model=ObjectUpdate)
def update_object_partial(object_id: int, update_data: ObjectUpdate, db: Session = Depends(get_db)):

    db_object = db.query(Object).filter(Object.id == object_id).first()
    if db_object is None:
        raise HTTPException(status_code=404, detail="Object not found")

    update_data_dict = update_data.dict(exclude_unset=True)
    for key, value in update_data_dict.items():
        if hasattr(db_object, key):
            setattr(db_object, key, value)

    db.commit()
    db.refresh(db_object)

    return db_object

