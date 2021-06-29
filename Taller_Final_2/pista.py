# Variable global
undefined = "Unknown"

# Clase piloto
class Pista:
    nombre_pista = undefined
    tipo_exigencia_1 = undefined
    tipo_exigencia_2 = undefined
    

    # Definición del método constructor
    def __init__(self, nombre_pista, tipo_exigencia_1, tipo_exigencia_2):
        self.nombre_pista = nombre_pista
        self.tipo_exigencia_1 = tipo_exigencia_1
        self.tipo_exigencia_2 = tipo_exigencia_2
