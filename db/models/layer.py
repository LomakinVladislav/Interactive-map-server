from db.base_class import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Layer(Base):
    id = Column(Integer, primary_key=True, index=True)
    color = Column(String, nullable = False)
    description = Column(String, nullable = False)

