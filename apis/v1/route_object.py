from fastapi import APIRouter, HTTPException, status, Query
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends

from db.models.boundaries import Boundaries
from db.models.city_and_project import City_and_project
from db.models.layer import Layer
from schemas.boundaries import BoundariesShow
from schemas.object import ObjectCreate,ObjectShow,ObjectUpdate,ObjectDetails
from db.session import get_db
from db.repository.object import create_new_object,retrieve_object
from db.models.object import Object
from typing import List,Optional

router = APIRouter()

@router.post("/objects/", response_model=ObjectShow, status_code=status.HTTP_201_CREATED)
def add_object(object_data: ObjectCreate, db: Session = Depends(get_db)):
    """
     Добавляет информацию об объекте недвижимости.
    """
    try:
        new_object = create_new_object(object_data=object_data, db=db)
        return new_object
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при создании объекта: {e}")


@router.get("/object/{object_id}", response_model=ObjectShow, status_code=status.HTTP_200_OK)
def get_object(object_id: int, db: Session = Depends(get_db)):
    """
        Получает информацию об объекте недвижимости по его ID.
    """
    object_item = retrieve_object(db=db, object_id=object_id)
    if object_item is None:
        raise HTTPException(status_code=404, detail="Объект не найден.")
    return object_item

@router.patch("/objects/{object_id}", response_model=ObjectUpdate)
def update_object_partial(object_id: int, update_data: ObjectUpdate, db: Session = Depends(get_db)):
    """
    Обновляет информацию об объекте недвижимости по его ID.
    """
    db_object = db.query(Object).filter(Object.id == object_id).first()
    if db_object is None:
        raise HTTPException(status_code=404, detail="Объект не найден.")

    update_data_dict = update_data.dict(exclude_unset=True)
    for key, value in update_data_dict.items():
        if hasattr(db_object, key):
            setattr(db_object, key, value)

    db.commit()
    db.refresh(db_object)

    return db_object

@router.get("/{object_id}/cadastral_number", response_model=str)
def get_cadastral_number(object_id: int, db: Session = Depends(get_db)):
    """
       Получает кадастровый номер объекта недвижимости по его ID.
    """
    obj = db.query(Object).filter(Object.id == object_id).first()
    if obj is None:
        raise HTTPException(status_code=404, detail="Объект не найден.")
    return obj.cadastral_number

@router.get("/{object_id}/address", response_model=str)
def get_address(object_id: int, db: Session = Depends(get_db)):
    """
       Получает адрес объекта недвижимости по его ID.
    """
    obj = db.query(Object).filter(Object.id == object_id).first()
    if obj is None:
        raise HTTPException(status_code=404, detail="Объект не найден.")
    return obj.address

@router.get("/{object_id}/area", response_model=float)
def get_area(object_id: int, db: Session = Depends(get_db)):
    """
       Получает площадь объекта недвижимости по его ID.
    """
    obj = db.query(Object).filter(Object.id == object_id).first()
    if obj is None:
        raise HTTPException(status_code=404, detail="Объект не найден.")
    return obj.area


@router.get("/objects/details", response_model=List[ObjectDetails], status_code=status.HTTP_200_OK)
def get_all_object_details(db: Session = Depends(get_db)):
    """
       Получает кадастровые номера, площади и адреса всех объектов недвижимости.
    """
    objects = db.query(Object).all()
    if not objects:
        raise HTTPException(status_code=404, detail="Объекты не найдены.")

    return [ObjectDetails(
        cadastral_number=obj.cadastral_number,
        address=obj.address,
        area=obj.area
    ) for obj in objects]



class ObjectWithBoundaries(ObjectShow):
    boundaries: List[BoundariesShow]

    class Config:
        orm_mode = True


@router.get("/object/", response_model=List[ObjectWithBoundaries], status_code=status.HTTP_200_OK)
def read_objects_with_boundaries(

        object_type_id: Optional[int] = Query(None),
        layer_id: Optional[int] = Query(None),
        city: Optional[str] = Query(None),
        project_name: Optional[str] = Query(None),
        db: Session = Depends(get_db)
):

    query = db.query(Object).options(joinedload(Object.boundaries), joinedload(Object.object_type))

    if object_type_id is not None:
        query = query.filter(Object.object_type_id == object_type_id)

    if layer_id is not None:
        query = query.join(Boundaries).join(Layer).filter(Layer.id == layer_id)

    if city:
        query = query.filter(Object.city_and_project.has(City_and_project.city == city))

    if project_name:
        query = query.filter(Object.city_and_project.has(City_and_project.project_name == project_name))

    objects = query.all()
    if not objects:
        raise HTTPException(status_code=404, detail="Объекты не найдены по заданным критериям")

    return objects


