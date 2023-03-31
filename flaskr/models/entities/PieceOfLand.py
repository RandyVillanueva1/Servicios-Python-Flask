class PieceOfLand():

    def __init__(self, id_predio=None, id_propietario=None, num_manzana=None, num_lote=None, estatus=None, area=None, perimetro=None, num_vivienda=None, geom_predio=None, codigo_postal=None, colonia=None, num_catastral=None) -> None:
        self.id_predio = id_predio
        self.id_propietario = id_propietario
        self.num_manzana = num_manzana
        self.num_lote = num_lote
        self.estatus = estatus
        self.area = area
        self.perimetro = perimetro
        self.num_vivienda = num_vivienda
        self.geom_predio = geom_predio
        self.codigo_postal = codigo_postal
        self.colonia = colonia
        self.num_catastral = num_catastral

    def to_JSON(self):
        return {
            'id_predio': self.id_predio,
            'id_propietario': self.id_propietario,
            'num_manzana': self.num_manzana,
            'num_lote': self.num_lote,
            'estatus': self.estatus,
            'area': self.area,
            'perimetro': self.perimetro,
            'num_vivienda': self.num_vivienda,
            'geom_predio': self.geom_predio,
            'codigo_postal': self.codigo_postal,
            'colonia': self.colonia,
            'num_catastral': self.num_catastral
        }