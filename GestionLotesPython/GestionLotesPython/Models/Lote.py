from flask import Flask
from sqlal import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Decimal, Float
from sqlalchemy import create_engine

app = Flask(__name__)
app.debug = true
Base = declarative_base()

class Lote(Base):
    """description of class"""
    __tablename__ = 'lote'
    idLote = Column(Integer(), prymary_key=True)
    Direccion = Column(String(100))
    Numero = Column(String(10))
    Largo = Column(Float, nullable=True)
    Direccion = Column(Float, nullable=True)
    Hectareas = Column(Decimal(18.2))
    idCiudad = Column(Integer,ForeignKey('ciudad.idCiudad'))
    ciudad = relationship(Ciudad,backref=backref('lotes', uselist=True, cascade='delete,all'))
    idUsuario = Column(Integer,ForeignKey('usuario.idUsuario'))
    usuario = relationship(Usuario,backref=backref('lotes', uselist=True, cascade='delete,all'))


