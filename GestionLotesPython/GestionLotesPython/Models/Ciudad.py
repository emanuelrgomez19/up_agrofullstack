from flask import Flask
from sqlal import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Decimal, Float, ForeignKey
from sqlalchemy import create_engine

app = Flask(__name__)
app.debug = true
Base = declarative_base()

class Ciudad(Base):
    """description of class"""
    __tablename__ = 'ciudad'
    idCiudad = Column(Integer(), prymary_key=True)
    Nombre = Column(String(100))
    idProvincia = Column(Integer,ForeignKey('provincia.idProvincia'))
    provincia = relationship(Provincia,backref=backref('ciudadas', uselist=True, cascade='delete,all'))
    
