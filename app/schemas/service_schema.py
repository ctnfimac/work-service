from pydantic import BaseModel

class ServiceResponse(BaseModel):
    id: int
    description: str
    price: int
    gardener_id: int
    typeservice_id: int

    #class Config:
    #    orm_mode = True


class ServiceRequest(BaseModel):
    description: str
    price: int
    gardener_id: int
    typeservice_id: int