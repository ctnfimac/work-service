
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import TIMESTAMP, Column, Integer


class BaseModel:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()