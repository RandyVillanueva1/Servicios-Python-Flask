from flask import Blueprint, jsonify, request
from geoalchemy2.types import Geometry

# Entities
from models.entities.PieceOfLand import PieceOfLand
from models.entities.Owner import Owner

# Models
from models.PieceOfLandModel import PieceOfLandModel

predio = Blueprint('predio', __name__,)

@predio.route('/<id_propietario>')
def get_pieceOfLands(id_propietario):
    try:
        pieceOfLand = PieceOfLandModel.get_pieceOfLands(id_propietario)
        return jsonify(pieceOfLand)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@predio.route('/<id_propietario>/<id_predio>')
def get_pieceOfLand(id_usuario, id_propietario):
    try:
        pieceOfLand = PieceOfLandModel.get_pieceOfLand(id_usuario, id_propietario)
        if pieceOfLand != None:
            return jsonify(pieceOfLand)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@predio.route('/<id_propietario>/registroPredio', methods=['POST'])
def add_pieceOfLand():
    try:
        num_manzana = request.json['num_manzana']
        num_lote = request.json['num_lote']
        estatus = request.json['estatus']
        area = request.json['area']
        perimetro = request.json['perimetro']
        num_vivienda = request.json['num_vivienda']  
        geom_predio = Geometry(request.json['geom_predio'])
        codigo_postal = request.json['codigo_postal']
        colonia = request.json['colonia']
        num_catastral = request.json['num_catastral']          
        
        id_predio = int(request.json['id_predio'])
        id_propietario = Owner(request.json['id_propietario'])
        
        predio = PieceOfLand(id_predio, id_propietario, num_manzana, num_lote, estatus, area, perimetro, num_vivienda, geom_predio, codigo_postal, colonia, num_catastral)

        affected_rows = PieceOfLandModel.add_pieceOfLand(predio)

        if affected_rows == 1:
            return jsonify(predio.id_predio)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@predio.route('/<id_propietario>/<id_predio>/actualizarPredio', methods=['PUT'])
def update_pieceOfLand(id_predio):
    try:
        num_manzana = request.json['num_manzana']
        num_lote = request.json['num_lote']
        estatus = request.json['estatus']
        area = request.json['area']
        perimetro = request.json['perimetro']
        num_vivienda = request.json['num_vivienda']  
        geom_predio = Geometry(request.json['geom_predio'])
        codigo_postal = request.json['codigo_postal']
        colonia = request.json['colonia']
        num_catastral = request.json['num_catastral']          
        
        id_predio = int(request.json['id_predio'])
        id_propietario = Owner(request.json['id_propietario'])
        
        predio = PieceOfLand(id_predio, id_propietario, num_manzana, num_lote, estatus, area, perimetro, num_vivienda, geom_predio, codigo_postal, colonia, num_catastral)

        affected_rows = PieceOfLandModel.update_pieceOfLand(predio)

        if affected_rows == 1:
            return jsonify(predio.id_predio)
        else:
            return jsonify({'message': "No predio updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@predio.route('/<id_propietario>/<id_predio>/eliminarPredio', methods=['DELETE'])
def delete_pieceOfLand(id_predio):
    try:
        predio = PieceOfLand(id_predio)

        affected_rows = PieceOfLandModel.delete_pieceOfLand(predio)

        if affected_rows == 1:
            return jsonify(predio.id_predio)
        else:
            return jsonify({'message': "No predio deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500