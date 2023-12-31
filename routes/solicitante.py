from flask import Blueprint, request, jsonify
from models.solicitante import Solicitante, SolicitanteSchema
from utils.db import db

solicitante = Blueprint('solicitante', __name__)
solicitante_schema = SolicitanteSchema()


@solicitante.route('/solicitante', methods=['GET'])
def getSolicitante():
    if request.method == 'GET':
        data = {}
        solicitante = Solicitante.query.all()
        data["solicitante"] = solicitante
        return jsonify(solicitante_schema.dump(solicitante,many=True))
    
'''    
@solicitante.route('/add', methods=['POST'])
def addSolicitante():
    data = {}
    if request.method == 'POST':
        body = request.get_json()
        id_rol = body['id_rol']
        id_persona = body['id_persona']
        telefono = body['telefono']
        correo = body['correo']
        new_solicitante = Solicitante(correo,
                                      id_persona, id_rol,
                                      telefono)
        db.session.add(new_solicitante)
        db.session.commit()
        return jsonify(data)
'''

@solicitante.route('/solicitante/add', methods=['POST'])
def addSolicitante():
    if request.method == 'POST':
        solicitante_data = request.get_json()
        new_solicitante = solicitante_schema.load(solicitante_data, session=db.session)
        db.session.add(new_solicitante)
        db.session.commit()
        return jsonify(solicitante_schema.dump(new_solicitante))


"""""
@solicitante.route('/add', methods=['POST'])
def addSolicitante():
    data = {}
    if request.method == 'POST':
        body = request.get_json()
        tipo_identificacion = body['tipo_identificacion']
        numero_identificacion = body['numero_identificacion']
        telefono = body['telefono']
        
        new_solicitante = Solicitante(tipo_identificacion=tipo_identificacion,
                                      numero_identificacion=numero_identificacion, telefono=telefono)
        db.session.add(new_solicitante)
        db.session.commit()
        return jsonify(data)

@solicitante.route('/update', methods=['POST'])
def updateSolicitante():
    data = {}
    body = request.get_json()
    id_solicitante = body['id_solicitante']
    solicitante = Solicitante.query.get(id_solicitante)
    if request.method == 'POST':
        solicitante.nombres = body['nombres']
        solicitante.apellidos = body['apellidos']
        solicitante.tipo_identificacion = body['tipo_identificacion']
        solicitante.numero_identificacion = body['numero_identificacion']
        solicitante.telefono = body['telefono']
        db.session.commit()
    return jsonify(solicitante.to_dict())

@solicitante.route('/delete', methods=['POST'])
def deleteSolicitante():
    data = {}
    body = request.get_json()
    id_solicitante = body['id_solicitante']
    solicitante = Solicitante.query.get(id_solicitante)
    if request.method == 'POST':
        db.session.delete(solicitante)
        db.session.commit()
    return jsonify(data)

    """