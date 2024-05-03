from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.city_and_project import CityAndProjectCreate, ShowProject, ProjectName, City, CityAndProjectShow
from db.session import get_db
from db.repository.city_and_project import create_city_and_project,retrieve_city_and_project
from db.models.city_and_project import City_and_project
from typing import List


router = APIRouter()

@router.post("/city_and_project/", response_model=CityAndProjectShow, status_code=status.HTTP_201_CREATED)
def add_city_and_project(city_and_project_data: CityAndProjectCreate, db: Session = Depends(get_db)):
    """
    Создать новый проект.
    """
    try:
        new_city_and_project = create_city_and_project(city_and_project_data=city_and_project_data, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при создании проекта: {e}")

    return new_city_and_project

@router.get("/city_and_project/{city_and_project_id}", response_model=ShowProject)
def get_city_and_project(city_and_project_id: int, db: Session = Depends(get_db)):
    """
    Получить информацию о проекте по его ID.
    """
    status = retrieve_city_and_project(db=db, city_and_project_id=city_and_project_id)
    if not status:
        raise HTTPException(status_code=404, detail="Проект не найден")
    return status


@router.get("/cities/", response_model=List[City], status_code=status.HTTP_200_OK)
def get_all_cities(db: Session = Depends(get_db)):

    """ Получить список всех городов. """
    try:
        cities = db.query(City_and_project.city).distinct().all()
        cities = [City(city=city[0]) for city in cities]  # Преобразование списка кортежей в список строк
        return cities
    except:
        raise HTTPException(status_code=404, detail="Не удалось получить данные о городах")


@router.get("/projects/", response_model=List[ProjectName], status_code=status.HTTP_200_OK)
def get_all_projects(db: Session = Depends(get_db)):
    """
    Получить список всех проектов.
    """
    try:
        # Запрос на получение всех проектов
        projects = db.query(City_and_project.project_name).distinct().all()
        # Надлежащее преобразование каждого кортежа в экземпляр ProjectName
        projects_list = [ProjectName(project_name=project[0]) for project in projects]
        return projects_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Не удалось получить список проектов: {e}")