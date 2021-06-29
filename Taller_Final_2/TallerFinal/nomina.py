# Importo la librería random para utilizarlo en el cálculo del tiempo hecho por el piloto
import random

# Variable global
undefined = "Unknown"

# Calcular la nómina
    def calcular_nomina(self):
        # Director equipo: 10% bono por pole position

        # Lista ordenada
        pole_position = ejecutar.calcular_pole_position()
        piloto_ganador = pole_position[0]
        

        if self.equipo1.piloto1.nombre == piloto_ganador.nombre or self.equipo1.piloto2.nombre == piloto_ganador.nombre:
            print("GANADOR!: ", piloto_ganador.nombre, " : ", piloto_ganador.tiempo_piloto, " sg y pertenece al equipo equipo 1 ")
            beneficio_director = (4000 + 0.10)
            print("El suelto + beneficio para el director ", directores[0], " del equipo 1 es de: ", beneficio_director)
        elif self.equipo2.piloto1.nombre == piloto_ganador.nombre or self.equipo2.piloto2.nombre == piloto_ganador.nombre:
            print("GANADOR!: ", piloto_ganador.nombre, " : ", piloto_ganador.tiempo_piloto, " sg pertenece al equipo equipo 2 ")
            beneficio_director = (4000 + 0.10)
            print("El suelto + beneficio para el director ", directores[1], " del equipo 2 es de: ", beneficio_director)

        
    def calcular_nomina_pilotos(self):
         # Lista ordenada
        pole_position = ejecutar.calcular_pole_position()
        piloto_segunda_posición = pole_position[1]

        # Piloto: 10% extra si clasifica 2do o mejor
        #         20% si lo hace en una pista donde no tiene bono
        if self.equipo1.piloto2.nombre == piloto_segunda_posición.nombre or self.equipo1.piloto2.nombre == piloto_segunda_posición.nombre:
            print("Segunda posición: ", piloto_segunda_posición.nombre, " : ", piloto_segunda_posición.tiempo_piloto, " sg y pertenece al equipo 1")
            beneficio_segunda_posición = (2000 + 0.10)
            print("El sueldo + beneficio por segunda posición para el piloto ", piloto_segunda_posición.nombre, " del equipo 1 es de: ", beneficio_segunda_posición )
        elif self.equipo2.piloto1.nombre == piloto_segunda_posición.nombre or self.equipo2.piloto2.nombre == piloto_segunda_posición.nombre:
            print("Segunda posición: ", piloto_segunda_posición.nombre, " : ", piloto_segunda_posición.tiempo_piloto, " sg y pertenece al equipo 2")
            beneficio_segunda_posición = (2000 + 0.10)
            print("El sueldo + beneficio por segunda posición para el piloto ", piloto_segunda_posición.nombre, " del equipo 2 es de: ", beneficio_segunda_posición )


        # Mecánico: 5% extra si logra una parada en pits menor 2.2 segundos

