from db.base_class import Base
from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship


class Boundaries(Base):
    id = Column(Integer, primary_key=True, index=True)
    object_id = Column(Integer, ForeignKey("object.id"))
    layer_id = Column(Integer, ForeignKey("layer.id"))
    latitude = Column(Numeric, default=False)
    longitude = Column(Numeric, default=True)
