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

class Lote(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    direccion = db.Column(db.String(100))
    numero = db.Column(db.String(100))
    largo = db.Column(db.Integer(), nullable=True)
    hectareas = db.Column(db.Integer())
   # idCiudad = db.Column(db.Integer,ForeignKey('ciudad.id'))
    #ciudad = relationship(Ciudad,backref=backref('lotes', uselist=True, cascade='delete,all'))
    #idUsuario = db.Column(db.Integer,ForeignKey('usuario.id'))
   # usuario = relationship(Usuario,backref=backref('lotes', uselist=True, cascade='delete,all'))
   
      
    def __init__(self, direccion,numero,largo,hectareas):
        self.direccion = direccion
        self.numero = numero
        self.largo = largo
        self.hectareas = hectareas

    

db.create_all()

class LoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'direccion','numero','largo','hectareas')


lote_schema = LoteSchema()
lotes_schema = LoteSchema(many=True)


@app.route('/lotes', methods=['GET'])
def getLotes():
    all_lotes = Lote.query.all()
    result = lotes_schema.dump(all_lotes)
    return jsonify(result)

@app.route('/lote', methods=['POST'])
def setLote():
  direccion = request.json['direccion']
  numero = request.json['numero']
  largo = request.json['largo']
  hectareas = request.json['hectareas']

  new_lote = Lote(direccion,numero,largo,hectareas)
  
  db.session.add(new_lote)
  db.session.commit()
  return lote_schema.jsonify(new_lote)

@app.route('/lote/<id>', methods=['GET'])
def getLote(id):
  lote = Lote.query.get(id)
  return lote_schema.jsonify(lote)


@app.route('/lote/<id>', methods=['PUT'])
def updateCiudad(id):
  lote = Lote.query.get(id)
  lote.direccion = request.json['direccion']
  lote.numero = request.json['numero']
  lote.largo = request.json['largo']
  lote.hectareas = request.json['hectareas']
  db.session.commit()

  return lote_schema.jsonify(lote)



if __name__ == "__main__":
    app.run(debug=True)