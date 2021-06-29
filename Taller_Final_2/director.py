import empleados

# Variable global
undefined = "Unknown"

# Clase director
class Director(empleados.Empleado):

    nombre = undefined
    salario = undefined
    nombre_equipo = undefined


    # Definición del método constructor
    def __init__(self, nombre, salario,nombre_equipo):
        self.nombre = nombre
        self.salario = salario
        self.nombre_equipo = nombre_equipo