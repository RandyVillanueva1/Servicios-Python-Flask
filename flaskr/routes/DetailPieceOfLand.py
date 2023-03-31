from flask import Blueprint, jsonify, request

# Entities
from models.entities.DetailPieceOfLand import DetailPieceOfLand
from models.entities.PieceOfLand import PieceOfLand

# Models
from models.DetailPieceOfLandModel import DetailPieceOfLandModel

detallePredio = Blueprint('detallePredio', __name__, url_prefix='/api/detallePredio')

@detallePredio.route('/<id_predio>')
def get_detailPieceOfLands(id_predio):
    try:
        detailPieceOfLand = DetailPieceOfLand.get_detailPieceOfLands(id_predio)
        return jsonify(detailPieceOfLand)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@detallePredio.route('/<id_predio>/<id_detalle>')
def get_detailPieceOfLand(id_usuario, id_propietario):
    try:
        detailPieceOfLand = DetailPieceOfLand.get_detailPieceOfLand(id_usuario, id_propietario)
        if detailPieceOfLand != None:
            return jsonify(detailPieceOfLand)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@detallePredio.route('/<id_predio>/registroDetallePredio', methods=['POST'])
def add_detailPieceOfLand():
    try:
        uso_suelo = request.json['uso_suelo']
        num_niveles = request.json['num_niveles']
        altura = request.json['altura']
        area_libre = request.json['area_libre']
        num_vivienda_p = request.json['num_vivienda_p']
        superficie_maxima = request.json['superficie_maxima']  
        densidad = request.json['densidad']     
        
        id_detalle = int(request.json['id_detalle'])
        id_predio = PieceOfLand(request.json['id_predio'])
        
        detallePredio = DetailPieceOfLand(id_detalle, id_predio, uso_suelo, num_niveles, altura, area_libre, num_vivienda_p, superficie_maxima, densidad)

        affected_rows = DetailPieceOfLandModel.add_detailPieceOfLand(detallePredio)

        if affected_rows == 1:
            return jsonify(detallePredio.id_detalle)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@detallePredio.route('/<id_predio>/<id_detalle>/actualizarDetallePredio', methods=['PUT'])
def update_detailPieceOfLand(id_detalle):
    try:
        uso_suelo = request.json['uso_suelo']
        num_niveles = request.json['num_niveles']
        altura = request.json['altura']
        area_libre = request.json['area_libre']
        num_vivienda_p = request.json['num_vivienda_p']
        superficie_maxima = request.json['superficie_maxima']  
        densidad = request.json['densidad']     
        
        id_detalle = int(request.json['id_detalle'])
        id_predio = PieceOfLand(request.json['id_predio'])
        
        detallePredio = DetailPieceOfLand(id_detalle, id_predio, uso_suelo, num_niveles, altura, area_libre, num_vivienda_p, superficie_maxima, densidad)

        affected_rows = DetailPieceOfLandModel.update_detailPieceOfLand(detallePredio)

        if affected_rows == 1:
            return jsonify(detallePredio.id_detalle)
        else:
            return jsonify({'message': "No detallePredio updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@detallePredio.route('/<id_predio>/<id_detalle>/eliminarDetallePredio', methods=['DELETE'])
def delete_detailPieceOfLand(id_detalle):
    try:
        detallePredio = DetailPieceOfLand(id_detalle)

        affected_rows = DetailPieceOfLandModel.delete_detailPieceOfLand(detallePredio)

        if affected_rows == 1:
            return jsonify(detallePredio.id_detalle)
        else:
            return jsonify({'message': "No detallePredio deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500