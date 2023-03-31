from database.db import get_connection
from models.entities.DetailPieceOfLand import DetailPieceOfLand

class DetailPieceOfLandModel():

    @classmethod
    def get_detailPieceOfLands(self, id_predio):
        try:
            connection = get_connection()
            detailPieceOfLands = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_detalle, id_predio, uso_suelo, num_niveles, altura, area_libre, num_vivienda_p, superficie_maxima, densidad FROM detalles_predio WHERE id_predio = %s", (id_predio))
                resultset = cursor.fetchall()

                for row in resultset:
                    detailPieceOfLand = DetailPieceOfLand(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    detailPieceOfLands.append(detailPieceOfLand.to_JSON())

            connection.close()
            return detailPieceOfLands
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_detailPieceOfLand(self, id_detalle):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_detalle, id_predio, uso_suelo, num_niveles, altura, area_libre, num_vivienda_p, superficie_maxima, densidad FROM detalles_predio WHERE id_detalle = %s", (id_detalle))
                row = cursor.fetchone()

                detailPieceOfLand = None
                if row != None:
                    detailPieceOfLand = DetailPieceOfLand(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    detailPieceOfLand = detailPieceOfLand.to_JSON()

            connection.close()
            return detailPieceOfLand
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_detailPieceOfLand(self, detallePredio):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO detalles_predio (id_detalle, uso_suelo, num_niveles, altura, area_libre, num_vivienda_p, superficie_maxima,  FOREIGN KEY(id_predio) REFERENCES predios(id_predio) ON DELETE CASCADE) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""", 
                (detallePredio.id_detalle, detallePredio.id_predio, detallePredio.uso_suelo, detallePredio.num_niveles, detallePredio.altura, detallePredio.area_libre, detallePredio.num_vivienda_p, detallePredio.superficie_maxima, detallePredio.densidad))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_detailPieceOfLand(self, detallePredio):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE detalles_predio SET uso_suelo = %s, num_niveles = %s, altura = %s, area_libre = %s, num_vivienda_p = %s, superficie_maxima = %s, densidad = %s,
                                WHERE id_detalle = %s and id_predio = %s """, (detallePredio.id_detalle, detallePredio.id_predio, detallePredio.uso_suelo, detallePredio.num_niveles, detallePredio.altura, detallePredio.area_libre, detallePredio.num_vivienda_p, detallePredio.superficie_maxima, detallePredio.densidad))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_detailPieceOfLand(self, detallePredio):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM detalles_predio WHERE id_detalle = %s and id_predio = %s", (detallePredio.id_detalle, detallePredio.id_predio,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)