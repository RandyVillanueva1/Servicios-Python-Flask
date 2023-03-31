from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Owner import Owner
from models.entities.User import User

# Models
from models.OwnerModel import OwnerModel

propietario = Blueprint('propietario', __name__, url_prefix='/api/propietario')


@propietario.route('/<id_usuario>')
def get_owners(id_usuario):
    try:
        owners = OwnerModel.get_owners(id_usuario)
        return jsonify(owners)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@propietario.route('/<id_usuario>/<id_propietario>')
def get_owner(id_usuario, id_propietario):
    try:
        propietario = OwnerModel.get_owner(id_usuario, id_propietario)
        if propietario != None:
            return jsonify(propietario)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@propietario.route('/<id_usuario>/registroPropietario', methods=['POST'])
def add_owner():
    try:
        nombre = request.json['nombre']
        apellido_pa = request.json['apellido_pa']
        apellido_ma = request.json['apellido_ma']
        fecha_nacimiento = request.json['fecha_nacimiento']
        genero = request.json['genero']
        correo = request.json['correo']  
        contrasena = request.json['contrasena']
        public_id = request.json['public_id']
        curp = request.json['curp']       
        
        id_usuario = int(request.json['id_usuario'])
        id_propietario = int(request.json['id_propietario'])
        
        propietario = Owner(id_propietario, nombre, apellido_pa, apellido_ma, fecha_nacimiento, genero, correo, contrasena, public_id, curp, id_usuario)

        affected_rows = OwnerModel.add_owner(propietario)

        if affected_rows == 1:
            return jsonify(propietario.id_propietario)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@propietario.route('/<id_propietario>/actualizarUsuario', methods=['PUT'])
def update_owner(id_propietario):
    try:
        nombre = request.json['nombre']
        apellido_pa = request.json['apellido_pa']
        apellido_ma = request.json['apellido_ma']
        fecha_nacimiento = request.json['fecha_nacimiento']
        genero = request.json['genero']
        correo = request.json['correo']  
        contrasena = request.json['contrasena']
        public_id = request.json['public_id']
        curp = request.json['curp']   
        
        id_usuario = User(request.json['id_usuario'])
        id_propietario = int(request.json['nombre'])
        
        propietario = Owner(id_propietario, nombre, apellido_pa, apellido_ma, fecha_nacimiento, genero, correo, contrasena, public_id, curp, id_usuario)

        affected_rows = OwnerModel.update_owner(propietario)

        if affected_rows == 1:
            return jsonify(propietario.id_propietario)
        else:
            return jsonify({'message': "No propietario updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@propietario.route('/<id_usuario>/<id_propietario>/eliminarUsuario', methods=['DELETE'])
def delete_owner(id_propietario):
    try:
        propietario = Owner(id_propietario)

        affected_rows = OwnerModel.delete_owner(propietario)

        if affected_rows == 1:
            return jsonify(propietario.id_propietario)
        else:
            return jsonify({'message': "No propietario deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500