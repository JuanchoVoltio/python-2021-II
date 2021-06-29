import simulacion
import datos

class Nomina:
    # Objeto para acceder a la clase simulación
    simulacion = simulacion.Simuladores()
    # Objeto para acceder a la clase datos
    datos = datos.Datos()

    
    # calcular nomina piloto primer puesto
    def calcular_nomina_primer_lugar(self,pole_position):
        # Lista ordenada
        #pole_position = self.simulacion.calcular_pole_position()
        piloto_ganador = pole_position[0]

        print("##### NÓMINA PILOTO PRIMER LUGAR POLE POSITION #####")

        if piloto_ganador.nombre_equipo == "Equipo 1":
            print("1. ", piloto_ganador.nombre, " : ", piloto_ganador.tiempo_piloto, " sg y pertenece al equipo equipo 1 ")
            beneficio_primer_puesto = ((piloto_ganador.salario * 0.1) + float(piloto_ganador.salario))
            print("El sueldo + beneficio para el piloto ", piloto_ganador.nombre, " del equipo 1 es de: $ ", beneficio_primer_puesto)
        elif piloto_ganador.nombre_equipo == "Equipo 2":
            print("1. ", piloto_ganador.nombre, " : ", piloto_ganador.tiempo_piloto, " sg pertenece al equipo equipo 2 ")
            beneficio_primer_puesto = ((piloto_ganador.salario * 0.1) + float(piloto_ganador.salario))
            print("El sueldo + beneficio para el piloto ", piloto_ganador.nombre, " del equipo 2 es de: $ ", beneficio_primer_puesto)

        
    def calcular_nomina_segundo_lugar(self,pista_seleccionada,pole_position):
         # Lista ordenada
        #pole_position = self.simulacion.calcular_pole_position()
        piloto_segunda_posicion = pole_position[1]
        print("##### NÓMINA PILOTO SEGUNDA LUGAR POLE POSITION #####")
        # Piloto: 10% extra si clasifica 2do o mejor
        #         20% si lo hace en una pista donde no tiene bono
        if piloto_segunda_posicion.nombre_equipo == "Equipo 1":
            print(pista_seleccionada)            
            if  pista_seleccionada.tipo_exigencia_1 != piloto_segunda_posicion.bono_piloto and pista_seleccionada.tipo_exigencia_2 != piloto_segunda_posicion.bono_piloto:
                print("2. ", piloto_segunda_posicion.nombre, " : ", piloto_segunda_posicion.tiempo_piloto, " sg y pertenece al equipo 1")
                beneficio_segunda_posición = ((piloto_segunda_posicion.salario * 0.2) + float(piloto_segunda_posicion.salario))
                print("El sueldo + beneficio por segunda posición para el piloto ", piloto_segunda_posicion.nombre, " del equipo 1 es de: $ ", beneficio_segunda_posición )
            print("El sueldo por segunda posición para el piloto ", piloto_segunda_posicion.nombre, " del equipo 1 es de: ", piloto_segunda_posicion.salario)
        elif piloto_segunda_posicion.nombre_equipo == "Equipo 2":
            if  pista_seleccionada.tipo_exigencia_1 != piloto_segunda_posicion.bono_piloto and pista_seleccionada.tipo_exigencia_2 != piloto_segunda_posicion.bono_piloto:
                print("2.", piloto_segunda_posicion.nombre, " : ", piloto_segunda_posicion.tiempo_piloto, " sg y pertenece al equipo 2")
                beneficio_segunda_posición = ((piloto_segunda_posicion.salario * 0.2) + float(piloto_segunda_posicion.salario))
                print("El sueldo + beneficio por segunda posición para el piloto ", piloto_segunda_posicion.nombre, " del equipo 2 es de: $ ", beneficio_segunda_posición )
            print("El sueldo por segunda posición para el piloto ", piloto_segunda_posicion.nombre, " del equipo 2 es de: ", piloto_segunda_posicion.salario)
        
        
        
        
    # Calcular la nómina para los directores
    def calcular_nomina_directores(self,pole_position):
        # Director equipo: 10% bono por pole position

        # Lista ordenada
        #pole_position = self.simulacion.calcular_pole_position()
        piloto_ganador = pole_position[0]
        directores = self.datos.obtener_Director()
        print("##### NÓMINA DIRECTORES #####")
        for i in(directores):
            if i.nombre_equipo == "Equipo 1":                  
                if piloto_ganador.nombre_equipo == "Equipo 1":
                    beneficio_director = ((i.salario * 0.1) + i.salario)
                    print("El sueldo + beneficio para el director ", i.nombre , " del equipo 1 es de: $ ", beneficio_director)
                    #print("El sueldo + beneficio para el director ", directores[0], " del equipo 1 es de: ", beneficio_director)
            elif i.nombre_equipo == "Equipo 2":                  
                if piloto_ganador.nombre_equipo == "Equipo 2":
                    beneficio_director = ((i.salario * 0.1) + i.salario)
                    #print("El sueldo + beneficio para el director ", directores[1], " del equipo 2 es de: ", beneficio_director)
                    print("El sueldo + beneficio para el director ",i.nombre, " del equipo 2 es de: $ ", beneficio_director)

    

    # Calcular la nómina para los mecánicos
     # Mecánico: 5% extra si logra una parada en pits menor 2.2 segundos
    def calcular_nomina_mecanicos(self):
        print("##### NÓMINA MECÁNICOS #####")

        mecanicos = self.datos.obtener_Mecanico()
        
        for i in (mecanicos):
            tiempo_total_mecanico = self.simulacion.calcular_tiempo_pits()
            i.tiempo_mecanico = tiempo_total_mecanico
            
            if i.nombre_equipo == "Equipo 1":
                if i.tiempo_mecanico <= 2.2:
                    beneficio_mecanico = ((i.salario * 0.5) + i.salario)
                    print("El mecánico ", i.nombre, " que pertenece al equipo ", i.nombre_equipo," hizo un tiempo de: ", i.tiempo_mecanico, "El salario + beneficio es de: $ ", beneficio_mecanico)
                    print(" ")
                else:
                    print("El mecánico ", i.nombre, " que pertenece al equipo ", i.nombre_equipo," hizo un tiempo de: ", i.tiempo_mecanico, "El salario es de: $ ", i.salario)
                    print(" ")
            elif i.nombre_equipo == "Equipo 2": 
                if i.tiempo_mecanico <= 2.2:
                    beneficio_mecanico = ((i.salario * 0.5) + i.salario)
                    print("El mecánico ", i.nombre, " que pertenece al equipo ", i.nombre_equipo," hizo un tiempo de: ", i.tiempo_mecanico, "El salario + beneficio es de: $ ", beneficio_mecanico)
                    print(" ")
                else:
                    print("El mecánico ", i.nombre, " que pertenece al equipo ", i.nombre_equipo," hizo un tiempo de: ", i.tiempo_mecanico, "El salario es de: $ ", i.salario)
                

# Objeto para llamar los métodos de la clase actual
ejecucion = Nomina()

#ejecucion.calcular_nomina_segundo_lugar("Suzuka")
#ejecucion.calcular_nomina_primer_lugar()
#ejecucion.calcular_nomina_mecanicos()
