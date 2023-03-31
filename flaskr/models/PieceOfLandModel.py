from database.db import get_connection
from models.entities.PieceOfLand import PieceOfLand

class PieceOfLandModel():

    @classmethod
    def get_pieceOfLands(self, id_propietario):
        try:
            connection = get_connection()
            pieceOfLands = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_predio, id_propietario, num_manzana, num_lote, estatus, area, perimetro, num_vivienda, geom_predio, codigo_postal, colonia, num_catastral FROM predios WHERE id_propietario = %s", (id_propietario))
                resultset = cursor.fetchall()

                for row in resultset:
                    pieceOfLand = PieceOfLand(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    pieceOfLands.append(pieceOfLand.to_JSON())

            connection.close()
            return pieceOfLands
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_pieceOfLand(self, id_predio):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_predio, id_propietario, num_manzana, num_lote, estatus, area, perimetro, num_vivienda, geom_predio, codigo_postal, colonia, num_catastral FROM predios WHERE id_predio = %s", (id_predio))
                row = cursor.fetchone()

                predio = None
                if row != None:
                    predio = PieceOfLand(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    predio = predio.to_JSON()

            connection.close()
            return predio
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_pieceOfLand(self, predio):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO predios (id_predio, num_manzana, num_lote, estatus, area, perimetro, num_vivienda, geom_predio, codigo_postal, colonia, num_catastral FOREIGN KEY(id_propietario) REFERENCES propietarios(id_propietario) ON DELETE CASCADE) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", 
                (predio.id_predio, predio.id_propietario, predio.num_manzana, predio.num_lote, predio.estatus, predio.area, predio.perimetro, predio.num_vivienda, predio.geom_predio, predio.codigo_postal, predio.colonia, predio.num_catastral))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_pieceOfLand(self, predio):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE predios SET num_manzana = %s, num_lote = %s, estatus = %s, area = %s, perimetro = %s, num_vivienda = %s, geom_predio = %s, codigo_postal = %s, colonia = %s, num_catastral = %s,
                                WHERE id_predio = %s and id_propietario = %s """, (predio.id_predio, predio.id_propietario, predio.num_manzana, predio.num_lote, predio.estatus, predio.area, predio.perimetro, predio.num_vivienda, predio.geom_predio, predio.codigo_postal, predio.colonia, predio.num_catastral))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_pieceOfLand(self, predio):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM predios WHERE id_predio = %s and id_propietario = %s", (predio.id_propietario, predio.id_propietario,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)