from sqlalchemy import Column, Integer, String
from db.base_class import Base
from sqlalchemy.orm import relationship

class Redemption_status(Base):
    id = Column(Integer, primary_key = True, index = True)
    status_name = Column(String, nullable = False)


