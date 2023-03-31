class DetailPieceOfLand():

    def __init__(self, id_detalle=None, id_predio=None, uso_suelo=None, num_niveles=None, altura=None, area_libre=None, num_vivienda_p=None, superficie_maxima=None, densidad=None) -> None:
        self.id_detalle = id_detalle
        self.id_predio = id_predio
        self.uso_suelo = uso_suelo
        self.num_niveles = num_niveles
        self.altura = altura
        self.area_libre = area_libre
        self.num_vivienda_p = num_vivienda_p
        self.superficie_maxima = superficie_maxima
        self.densidad = densidad

    def to_JSON(self):
        return {
            'id_detalle': self.id_detalle,
            'id_predio': self.id_predio,
            'uso_suelo': self.uso_suelo,
            'num_niveles': self.num_niveles,
            'altura': self.altura,
            'area_libre': self.area_libre,
            'num_vivienda_p': self.num_vivienda_p,
            'superficie_maxima': self.superficie_maxima,
            'densidad': self.densidad
        }