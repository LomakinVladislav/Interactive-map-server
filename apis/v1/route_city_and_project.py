from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.city_and_project import CityAndProjectCreate,ShowStatus
from db.session import get_db
from db.repository.city_and_project import create_city_and_project,retrieve_city_and_project

router = APIRouter()


@router.post("/city_and_project/", response_model=ShowStatus, status_code=status.HTTP_201_CREATED)
def add_city_and_project(city_and_project_data: CityAndProjectCreate, db: Session = Depends(get_db)):
    """
    Создать новый проект.
    """
    try:
        new_city_and_project = create_city_and_project(city_and_project_data=city_and_project_data, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при создании проекта: {e}")

    return new_city_and_project

@router.get("/city_and_project/{city_and_project_id}", response_model=ShowStatus)
def get_city_and_project(city_and_project_id: int, db: Session = Depends(get_db)):
    """
    Получить информацию о проекте по его ID.
    """
    status = retrieve_city_and_project(db=db, city_and_project_id=city_and_project_id)
    if not status:
        raise HTTPException(status_code=404, detail="Статус выкупа не найден")
    return status
