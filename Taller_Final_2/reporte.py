import nomina
import simulacion
import datos

class Reporte():

    # Objeto para acceder a la clase nómina
    mi_nomina = nomina.Nomina()

    # Objeto para acceder a la clase simulacion
    mi_simulacion = simulacion.Simuladores()

    mi_pista = datos.Datos().obtener_Pistas()

    # Variable global
    undefined = "Unknown"

    print("Digite la pista que desea correr")
    print("Long Beach")
    print("Interlagos")
    print("Suzuka")
    print("Silverstone")
    ingreso_pista = input("¿Que pista correrán los pilotos?: ")
    print(ingreso_pista)

    pista_seleccionada = undefined

    if ingreso_pista == "Long Beach":
        pista_seleccionada = mi_pista[0]
    elif ingreso_pista == "Interlagos":
        pista_seleccionada = mi_pista[1]
    elif ingreso_pista == "Suzuka":
        pista_seleccionada = mi_pista[2]
    elif ingreso_pista == "Silverstone":
        pista_seleccionada = mi_pista[3]


    def reporte_Nomina(self):


        print("################## POLE POSITION #################")
        pilotos = self.mi_simulacion.calcular_pole_position()
        # Recorro la lista ordenada de pilotos con sus respectivos tiempos
        contador = 1
        for i in (pilotos):
            print(contador, ". ", i.nombre,i.tiempo_piloto, " sg" , i.bono_piloto, i.nombre_equipo)
            contador = contador + 1

        print(" ")
        self.mi_nomina.calcular_nomina_primer_lugar(pilotos)
        print(" ")
        self.mi_nomina.calcular_nomina_segundo_lugar(self.pista_seleccionada, pilotos)
        print(" ")
        self.mi_nomina.calcular_nomina_directores(pilotos)
        print(" ")
        self.mi_nomina.calcular_nomina_mecanicos()
        






ejecucion = Reporte()

ejecucion.reporte_Nomina()



        