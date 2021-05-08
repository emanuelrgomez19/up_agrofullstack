from flask import Flask, request, json, Response
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from sqlalchemy import Column, Integer, String
#from sqlalchemy import create_engine

session = sessionmaker()
session.configure(bind=engine)
app = Flask(__name__)
app.debug = True

@app.route('/ciudad', methods=['GET'])
def ciudad_list():
  ciudades = s.query(Ciudad)
  return Response(json.dumps(Ciudad), status=200, mimetype='application/json')

#@app.route('/proveedores', methods=['POST'])
#def create_provider():
    