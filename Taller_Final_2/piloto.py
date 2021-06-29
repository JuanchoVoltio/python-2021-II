import empleados

# Variable global
undefined = "Unknown"

# Clase piloto
class Piloto(empleados.Empleado):
    tiempo_piloto = undefined
    bono_piloto = undefined
    nombre_equipo = undefined

    # Definición del método constructor
    def __init__(self, nombre, salario, bono_piloto, nombre_equipo):
        self.nombre = nombre
        self.salario = salario
        self.bono_piloto = bono_piloto
        self.nombre_equipo = nombre_equipo