from flask import Flask
from sqlal import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Decimal, Float
from sqlalchemy import create_engine

app = Flask(__name__)
app.debug = true
Base = declarative_base()

class Documento(Base):
    """description of class"""
    __tablename__ = 'documento'
    idDocumento = Column(Integer(), prymary_key=True)
    TipoDocumento = Column(String(2))
    Numero = Column(String(20))    
    Total = Column(Decimal(18.2))


