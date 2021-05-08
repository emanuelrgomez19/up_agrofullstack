from flask import Flask, Request, JSON, Response
from click import Click
from sqlal import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

app = Flask(__name__)
app.debug = true
Base = declarative_base()

class Usuario(object):
    """description of class"""
    __tablename__ = 'usuario'
    idUsuario = Column(int, prymary_key=True)
    Direccion = Column(String(100))
    Numero = Column(String(10))
    UserName = Column(String(10), nullable=False)
    Password = Column(String(10), nullable=False)
    Mail = Column(String(10), nullable=False)


