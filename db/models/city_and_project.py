from sqlalchemy import Column, Integer, String, Numeric
from db.base_class import Base
from sqlalchemy.orm import relationship

class City_and_project(Base):
    id = Column(Integer, primary_key = True, index = True)
    city = Column(String, nullable = False)
    project_name = Column(String, nullable=False)
    center_latitude = Column(Numeric, default=True)
    center_longitude = Column(Numeric, default=True)
