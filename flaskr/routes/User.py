from flask import Blueprint, jsonify, request

# Entities
from models.entities.User import User
# Models
from models.UserModel import UserModel

usuario = Blueprint('usuario', __name__,)


@usuario.route('/')
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@usuario.route('/<id_usuario>')
def get_user(id_usuario):
    try:
        usuario = UserModel.get_user(id_usuario)
        if usuario != None:
            return jsonify(usuario)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@usuario.route('/registroUsuario', methods=['POST'])
def add_user():
    try:
        nombre = request.json['nombre']
        apellido_pa = request.json['apellido_pa']
        apellido_ma = request.json['apellido_ma']
        correo = request.json['correo']  
        contrasena = request.json['contrasena']       
        
        id_usuario = int(request.json['id_usuario'])
        usuario = User(int(id_usuario), nombre, apellido_pa, apellido_ma, correo, contrasena)

        affected_rows = UserModel.add_user(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id_usuario)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@usuario.route('/actualizarUsuario/<id_usuario>', methods=['PUT'])
def update_user(id_usuario):
    try:
        nombre = request.json['nombre']
        apellido_pa = request.json['apellido_pa']
        apellido_ma = request.json['apellido_ma']
        correo = request.json['correo']
        contrasena = request.json['contrasena'] 
        
        usuario = User(id_usuario, nombre, apellido_pa, apellido_ma, correo, contrasena)

        affected_rows = UserModel.update_user(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id_usuario)
        else:
            return jsonify({'message': "No usuario updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@usuario.route('/eliminarUsuario/<id_usuario>', methods=['DELETE'])
def delete_user(id_usuario):
    try:
        usuario = User(id_usuario)

        affected_rows = UserModel.delete_user(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id_usuario)
        else:
            return jsonify({'message': "No usuario deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500