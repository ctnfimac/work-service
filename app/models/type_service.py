from sqlalchemy import Column, String
from app.models.base_model import BaseModel
from db.base import Base

class TypeService(Base, BaseModel):
 
    __tablename__ = 'tipo_de_servicio'
 
    photo = Column("foto", String(50), unique=True, nullable=False)
    name = Column("nombre", String(30), unique=True, nullable=False)
    