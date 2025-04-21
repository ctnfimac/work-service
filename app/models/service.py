from sqlalchemy import Column, Integer, String, DECIMAL, UniqueConstraint
from models.base_model import BaseModel
from db.base import Base

class Service(Base, BaseModel):
 
    __tablename__ = 'servicio'
 
    description= Column("descripcion", String(100))
    price = Column("precio", DECIMAL(10, 2), nullable=False)
    gardener_id = Column("jardinero_id", Integer, nullable=False)
    typeservice_id = Column("tipodeservicio_id", Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('jardinero_id', 'tipodeservicio_id', name='unique_tipodeservicio_jardinero'),
    )

"""
Base = declarative_base()
"""