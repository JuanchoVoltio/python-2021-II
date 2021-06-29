import empleados

# Variable global
undefined = "Unknown"

# Clase mecánico
class Mecanico(empleados.Empleado):
    nombre = undefined
    tiempo_mecanico = undefined
    nombre_equipo = undefined
    

    # Definición del método constructor
    def __init__(self, nombre, salario, nombre_equipo):
        self.nombre = nombre
        self.salario = salario
        self.nombre_equipo = nombre_equipo
