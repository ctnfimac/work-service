from fastapi import APIRouter, HTTPException
from fastapi import Depends
from pymysql import IntegrityError
from sqlalchemy.orm import Session
from services.services_service import ServicesService
from db.base import get_db
from schemas.service_schema import ServiceRequest, ServiceResponse


router_service_controller = APIRouter()


@router_service_controller.get('/api/v1/services/', response_model=list[ServiceResponse])
def get_services(db: Session=Depends(get_db)):
    services_service = ServicesService(db)
    return services_service.getAll()


@router_service_controller.post('/api/v1/services/', response_model=ServiceResponse)
def create_service(service:ServiceRequest, db: Session=Depends(get_db)):
    services_service = ServicesService(db)
    return services_service.create(service)