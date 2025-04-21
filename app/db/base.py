import mysql.connector

from fastapi import FastAPI, HTTPException
from mysql.connector import Error

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


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()