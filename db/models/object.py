from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Object(Base):
    id = Column(Integer, primary_key=True)
    redemption_status_id = Column(Integer, ForeignKey("redemption_status.id"))
    city_and_project_id = Column(Integer, ForeignKey("city_and_project.id"))
    object_type_id = Column(Integer, ForeignKey("object_type.id"))
    redemption_status = relationship("Redemption_status")
    address = Column(String, nullable=False)
    area = Column(Numeric, nullable=False)
    cadastral_number = Column(String, nullable=False)
    redemption_cost = Column(String, nullable=False)
    redemption_period = Column(String, nullable=False)
    num_residents = Column(Integer, nullable=False)
    owner_ship_rights = Column(String, nullable=False)
    center_latitude = Column(Numeric, default=False)
    center_longitude = Column(Numeric, default=True)
    boundaries = relationship("Boundaries", back_populates="object")
    object_type = relationship("Object_type", backref="object")
    city_and_project = relationship("City_and_project", backref="objects")
    redemption_status = relationship("Redemption_status", backref="objects")