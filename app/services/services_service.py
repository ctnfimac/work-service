from schemas.service_schema import ServiceRequest
from models.service import Service
from repositories.services_repository import ServicesRepository
from sqlalchemy.orm import Session

class ServicesService:
    def __init__(self, db:Session):
        self.service_repository = ServicesRepository(db)

    def getAll(self) -> list[Service]:
        return self.service_repository.get_services()

    def create(self, service: ServiceRequest) -> Service:
        return self.service_repository.create_service(service)