import mysql.connector

from fastapi import FastAPI, HTTPException
from mysql.connector import Error
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DATABASE_URL = "mysql+pymysql://christian:123456@localhost:3306/work-database"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
def session_local():
    try:
        connection = mysql.connector.connect(
            host='localhost', 
            database='work-database',
            user='christian',
            password='123456'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")
"""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()