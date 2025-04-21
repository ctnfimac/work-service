from sqlalchemy import Column, Integer, String, Text
from app.models.base_model import BaseModel
from db.base import Base

class WorkCompleted(Base, BaseModel):
 
    __tablename__ = 'trabajo_realizado'
 
    photo = Column("foto", String(50), nullable=False)
    description = Column("descripcion", Text)
    gardener_id = Column("jardinero_id", Integer, nullable=False)
