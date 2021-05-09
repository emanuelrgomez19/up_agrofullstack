from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine

import pyodbc 

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@agroup'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Ciudad(db.Model):
    """description of class"""
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(100))
   
      
    def __init__(self, nombre):
        self.nombre = nombre
    

db.create_all()

class CiuadSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre')


ciudad_schema = CiuadSchema()
ciudades_schema = CiuadSchema(many=True)


@app.route('/ciudades', methods=['GET'])
def getCiudades():
    all_ciudades = Ciudad.query.all()
    result = ciudades_schema.dump(all_ciudades)
    return jsonify(result)

@app.route('/ciudad', methods=['POST'])
def setCiudad():
  nombre = request.json['nombre']
  new_ciudad = Ciudad(nombre)
  print(new_ciudad)
  db.session.add(new_ciudad)
  db.session.commit()
  return ciudad_schema.jsonify(new_ciudad)

@app.route('/ciudad/<id>', methods=['GET'])
def getCiudad(id):
  ciudad = Ciudad.query.get(id)
  return ciudad_schema.jsonify(ciudad)


@app.route('/ciudad/<id>', methods=['PUT'])
def updateCiudad(id):
  ciudad = Ciudad.query.get(id)
  nombre = request.json['nombre']
  ciudad.nombre = nombre
  db.session.commit()

  return ciudad_schema.jsonify(ciudad)



if __name__ == "__main__":
    app.run(debug=True)