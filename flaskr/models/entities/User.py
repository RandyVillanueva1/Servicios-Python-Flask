
class User():

    def __init__(self, id_usuario, nombre=None, apellido_pa=None, apellido_ma=None, correo=None, contrasena=None) -> None:
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido_pa = apellido_pa
        self.apellido_ma = apellido_ma
        self.correo = correo
        self.contrasena = contrasena

    def to_JSON(self):
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'apellido_pa': self.apellido_pa,
            'apellido_ma': self.apellido_ma,
            'correo': self.correo,
            'contrasena': self.contrasena,
        }