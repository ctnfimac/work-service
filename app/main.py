from typing import Union
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import FastAPI
from db.base import get_db
from api.v1.service_controller import router_service_controller

app = FastAPI()

app.include_router(router_service_controller)

#@app.get("/")
#def read_root(db: Session=Depends(get_db)):
    #cursor = db.cursor(dictionary=True)
    #cursor.execute("SELECT * FROM servicio")
    #resultado = cursor.fetchall()

    #return {"resultado": resultado}


