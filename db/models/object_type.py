from sqlalchemy import Column, Integer, String
from db.base_class import Base
from sqlalchemy.orm import relationship

class Object_type(Base):
    id = Column(Integer, primary_key = True, index = True)
    type = Column(String, nullable = False)



