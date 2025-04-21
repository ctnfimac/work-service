from fastapi import HTTPException
from pymysql import IntegrityError
from sqlalchemy.orm import Session
from models.service import Service
from schemas.service_schema import ServiceRequest

class ServicesRepository:
    
    def __init__(self, db: Session):
        self.db = db

    def get_services(self) -> list[Service]:
        return self.db.query(Service).all()
    
    def create_service(self, service: ServiceRequest) -> Service:
        new_service = Service(**service.model_dump())
        self.db.add(new_service)
        self.db.commit()
        self.db.refresh(new_service)
        return new_service
        