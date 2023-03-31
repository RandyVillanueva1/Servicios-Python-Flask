from utils.DateFormat import DateFormat

class Owner():

    def __init__(self, id_propietario, nombre=None, apellido_pa=None, apellido_ma=None, fecha_nacimiento=None, genero=None, correo=None, contrasena=None, public_id=None, curp=None, id_usuario=None) -> None:
        self.id_propietario = id_propietario
        self.nombre = nombre
        self.apellido_pa = apellido_pa
        self.apellido_ma = apellido_ma
        self.fecha_nacimiento= fecha_nacimiento
        self.genero= genero
        self.correo = correo
        self.contrasena = contrasena
        self.public_id= public_id
        self.curp= curp
        self.id_usuario= id_usuario

    def to_JSON(self):
        return {
            'id_propietario': self.id_propietario,
            'nombre': self.nombre,
            'apellido_pa': self.apellido_pa,
            'apellido_ma': self.apellido_ma,
            'fecha_nacimiento': DateFormat.convert_date(self.fecha_nacimiento),
            'genero': self.genero,
            'correo': self.correo,
            'contrasena': self.contrasena,
            'public_id': self.public_id,
            'curp': self.curp,
            'id_usuario': self.id_usuario
        }