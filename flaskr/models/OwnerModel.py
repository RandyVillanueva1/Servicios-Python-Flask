from database.db import get_connection
from models.entities.Owner import Owner

class OwnerModel():

    @classmethod
    def get_owners(self, id_usuario):
        try:
            connection = get_connection()
            owners = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_propietario, nombre, apellido_pa, apellido_ma, fecha_nacimiento, genero, correo, contrasena, public_id, curp, id_usuario FROM propietarios WHERE id_usuario = %s", (id_usuario))
                resultset = cursor.fetchall()

                for row in resultset:
                    propietario = Owner(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    owners.append(propietario.to_JSON())

            connection.close()
            return owners
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_owner(self, id_usuario, id_propietario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_propietario, nombre, apellido_pa, apellido_ma, fecha_nacimiento, genero, correo, contrasena, public_id, curp, id_usuario FROM propietarios WHERE id_propietario = %s and id_usuario = %s", (id_propietario, id_usuario))
                row = cursor.fetchone()

                propietario = None
                if row != None:
                    propietario = Owner(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                    propietario = propietario.to_JSON()

            connection.close()
            return propietario
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_owner(self, id_usuario, propietario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO propietarios (id_propietario, nombre, apellido_pa, apellido_ma, fecha_nacimiento, genero, correo, contrasena, public_id, curp FOREIGN KEY(id_usuario = %s) REFERENCES usuarios(id_usuario = %s ) ON DELETE CASCADE) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (id_usuario)
                (propietario.id_propietario, propietario.nombre, propietario.apellido_pa, propietario.apellido_ma, propietario.fecha_nacimiento, propietario.correo, propietario.correo, propietario.contrasena, propietario.public_id, propietario.curp, propietario.id_usuario))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_owner(self, propietario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE propietarios SET nombre = %s, apellido_pa = %s, apellido_ma = %s, fecha_nacimiento = %s, correo = %s, contrasena = %s, public_id = %s, curp = %s
                                WHERE id_propietario = %s and id_usuario = %s """, (propietario.id_propietario, propietario.nombre, propietario.apellido_pa, propietario.apellido_ma, propietario.fecha_nacimiento, propietario.correo, propietario.contrasena, propietario.public_id, propietario.curp, propietario.id_usuario))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_owner(self, propietario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM propietarios WHERE id_propietario = %s and id_usuario= %s", (propietario.id_propietario, propietario.id_usuario))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)