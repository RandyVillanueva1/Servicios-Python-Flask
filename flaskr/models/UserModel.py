from database.db import get_connection
from models.entities.User import User

class UserModel():

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_usuario, nombre, apellido_pa, apellido_ma, correo, contrasena FROM usuarios ORDER BY nombre ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    usuario = User(row[0], row[1], row[2], row[3], row[4], row[5])
                    users.append(usuario.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id_usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_usuario, nombre, apellido_pa, apellido_ma, correo, contrasena FROM usuarios WHERE id_usuario = %s", (id_usuario))
                row = cursor.fetchone()

                usuario = None
                if row != None:
                    usuario = User(row[0], row[1], row[2], row[3], row[4], row[5])
                    usuario = usuario.to_JSON()

            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuarios (id_usuario, nombre, apellido_pa, apellido_ma, correo, contrasena) 
                                VALUES (%s, %s, %s, %s, %s, %s);""", 
                (usuario.id_usuario, usuario.nombre, usuario.apellido_pa, usuario.apellido_ma, usuario.correo, usuario.contrasena))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE usuarios SET nombre = %s, apellido_pa = %s, apellido_ma = %s, correo = %s, contrasena = %s
                                WHERE id_usuario = %s""", (usuario.nombre, usuario.apellido_pa, usuario.apellido_ma, usuario.correo, usuario.contrasena, usuario.id_usuario))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_user(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (usuario.id_usuario,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)