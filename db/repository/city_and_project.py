from sqlalchemy.orm import Session
from db.models.city_and_project import City_and_project
from schemas.city_and_project import CityAndProjectCreate


def create_city_and_project(city_and_project_data: CityAndProjectCreate, db: Session):
    city_and_project = City_and_project(**city_and_project_data.dict())
    db.add(city_and_project)
    db.commit()
    db.refresh(city_and_project)
    return {"city": city_and_project.city, "project_name": city_and_project.project_name}


def retrieve_city_and_project(db: Session, city_and_project_id: int):
    return db.query(City_and_project).filter(City_and_project.id == city_and_project_id).first()
