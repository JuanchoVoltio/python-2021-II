# Importo la librería random para utilizarlo en el cálculo del tiempo hecho por el piloto
from math import pi
import random

# Variable global
undefined = "Unknown"



bono = ["chasis","motor","aerodinamica"]
pilotos = []
pistas = []
directores = ["J. Montoya", "T, Aprilla"]
mecanicos = []
# mecanicos = ["Chavez", "Villanueva", "Ramirez", "Duque", "Henao", "Quintero", "Avellaneda", "Ortiz"]
sueldos = []
nombre_Equipos = []


class Pista:
    # Definición de atributos
    nombre = undefined
    tipo_exigencia_1 = undefined
    tipo_exigencia_2 = undefined

    # Definición del método constructor
    def __init__(self, nombre, tipo_exigencia_1, tipo_exigencia_2):
        self.nombre = nombre
        self.tipo_exigencia_1 = tipo_exigencia_1
        self.tipo_exigencia_2 =  tipo_exigencia_2

class Equipo:
    # Definición de atributos
    nombre_Equipo = undefined
    director = undefined
    mecanico1 = undefined
    mecanico2 = undefined
    mecanico3 = undefined
    mecanico4 = undefined
    piloto1 = undefined
    piloto2 = undefined
    sueldo_Director = undefined
    sueldo_Mecanico = undefined
    sueldo_Piloto = undefined

    # Definición del método constructor
    def __init__(self, nombre_Equipo, director, mecanico1, mecanico2, mecanico3, mecanico4, piloto1, piloto2,sueldo_Director,sueldo_Mecanico,sueldo_Piloto):
        self.nombre_Equipo = nombre_Equipo
        self.director = director
        self.mecanico1 = mecanico1
        self.mecanico2 = mecanico2
        self.mecanico3 = mecanico3
        self.mecanico4 = mecanico4
        self.piloto1 = piloto1
        self.piloto2 = piloto2
        self.sueldo_Director = sueldo_Director
        self.sueldo_Mecanico = sueldo_Mecanico
        self.sueldo_Piloto = sueldo_Piloto

class Piloto:
    nombre = undefined
    tiempo_piloto = undefined
    bono_piloto = undefined

    # Definición del método constructor
    def __init__(self, nombre, bono_piloto):
        self.nombre = nombre
        self.bono_piloto = bono_piloto

class Mecanico:
    nombre = undefined
    tiempo_mecanico = undefined

    # Definición del método constructor
    def __init__(self, nombre):
        self.nombre = nombre


class Ejecutora:
    pista = []
    pilotos = []
    mecanicos = []
    sueldos = []
    nombre_Equipos = []
    
    
    # Crear pilotos y agregarlos al arreglo vacío
    piloto1 = Piloto("C. Muñoz", bono[0])
    piloto2 = Piloto("Kobayashi", bono[1])
    piloto3 = Piloto("G. Chavez", bono[2])
    piloto4 = Piloto("P. Wherlein", bono[1])
    
    pilotos.append(piloto1)
    pilotos.append(piloto2)
    pilotos.append(piloto3)
    pilotos.append(piloto4)
    


    # Crear mecánicos y agregarlos al arreglo vacío
    mecanico1 = Mecanico("Chavez")
    mecanico2 = Mecanico("Villanueva")
    mecanico3 = Mecanico("Ramirez")
    mecanico4 = Mecanico("Duque")
    mecanico5 = Mecanico("Henao")
    mecanico6 = Mecanico("Quintero")
    mecanico7 = Mecanico("Avellaneda")
    mecanico8 = Mecanico("Ortiz")

    mecanicos.append(mecanico1)
    mecanicos.append(mecanico2)
    mecanicos.append(mecanico3)
    mecanicos.append(mecanico4)
    mecanicos.append(mecanico5)
    mecanicos.append(mecanico6)
    mecanicos.append(mecanico7)
    mecanicos.append(mecanico8)


    #Crear pistas con sus respectivas exigencias  
    pista1 = Pista("Long Beach",bono[0],bono[2])
    pista2 = Pista("Interlagos",bono[1],bono[0])
    pista3 = Pista("Suzuka",bono[2],bono[0])
    pista4 = Pista("Silverstone",bono[1],bono[2])

   
    
    #Crear equipos
    equipo1 = Equipo("Equipo 1",directores[0],mecanicos[0],mecanicos[1],mecanicos[2],mecanicos[3],pilotos[0],pilotos[1],4000,3000,2000)
    equipo2 = Equipo("Equipo 2",directores[1],mecanicos[4],mecanicos[5],mecanicos[6],mecanicos[7],pilotos[2],pilotos[3],4000,3000,2000)
    
    print("Seleccione el número de la pista que desea correr")
    print("1 = Long Beach")
    print("2 = Interlagos")
    print("3 = Suzuka")
    print("4 = Silverstone")
    ingreso_pista = int(input("¿Que pista correrán los pilotos?: "))
    print(ingreso_pista)

    pista_seleccionada = undefined

    if ingreso_pista == 1:
        #print("ENTRE")
        pista_seleccionada = pista1
    elif ingreso_pista == 2:
        pista_seleccionada = pista2
    elif ingreso_pista == 3:
        pista_seleccionada = pista3
    elif ingreso_pista == 4:
        pista_seleccionada = pista4
    


    #Retorna el tiempo del piloto
    def calcular_pole_position(self):
        # Recorrer el listado de pilotos
        for i in self.pilotos:
            # Calcular el tiempo por medio de este random
            tiempo_piloto = random.randint(1,70)
            # A cada piloto le guardo el tiempo que obtuvo
            i.tiempo_piloto = tiempo_piloto
            # print("El tiempo del piloto ", i.nombre, " es: ", i.tiempo_piloto)
        
        #for j in self.pilotos:
         #   print("Actualizacion ", j.nombre, " es: ", j.tiempo_piloto)
        
        # Ordenar el tiempo de los pilotos de menor a mayor
        n = len(self.pilotos)
        l = len(self.pilotos)

        for i in range(1,len(self.pilotos)):
            for j in range(0,len(self.pilotos)-i):
                if(self.pilotos[j+1].tiempo_piloto < self.pilotos[j].tiempo_piloto):
                    temp = self.pilotos[j]
                    self.pilotos[j] = self.pilotos[j+1]
                    self.pilotos[j+1] = temp       
        
        return self.pilotos

    # Calcular tiempo en pits de los mecánicos
    def calcular_tiempo_pits(self):
        tiempo_mecanico = random.randint(1,3)
        return tiempo_mecanico
    

    # calcular nomina piloto primer puesto
    def calcular_nomina_primer_lugar(self):
        # Lista ordenada
        pole_position = ejecutar.calcular_pole_position()
        piloto_ganador = pole_position[0]

        if self.equipo1.piloto1.nombre == piloto_ganador.nombre or self.equipo1.piloto2.nombre == piloto_ganador.nombre:
            print("GANADOR!: ", piloto_ganador.nombre, " : ", piloto_ganador.tiempo_piloto, " sg y pertenece al equipo equipo 1 ")
            beneficio_primer_puesto = (2000 + 0.10)
            print("El sueldo + beneficio para el piloto ", piloto_ganador.nombre, " del equipo 1 es de: ", beneficio_primer_puesto)
        elif self.equipo2.piloto1.nombre == piloto_ganador.nombre or self.equipo2.piloto2.nombre == piloto_ganador.nombre:
            print("GANADOR!: ", piloto_ganador.nombre, " : ", piloto_ganador.tiempo_piloto, " sg pertenece al equipo equipo 2 ")
            beneficio_primer_puesto = (2000 + 0.10)
            print("El sueldo + beneficio para el director ", piloto_ganador.nombre, " del equipo 2 es de: ", beneficio_primer_puesto)

        
    def calcular_nomina_segundo_lugar(self):
         # Lista ordenada
        pole_position = ejecutar.calcular_pole_position()
        piloto_segunda_posicion = pole_position[1]

        # Piloto: 10% extra si clasifica 2do o mejor
        #         20% si lo hace en una pista donde no tiene bono
        if self.equipo1.piloto1.nombre == piloto_segunda_posicion.nombre or self.equipo1.piloto2.nombre == piloto_segunda_posicion.nombre:
            if self.pista_seleccionada.tipo_exigencia_1 != piloto_segunda_posicion.bono_piloto and self.pista_seleccionada.tipo_exigencia_2 != piloto_segunda_posicion.bono_piloto:
                print("Segunda posición: ", piloto_segunda_posicion.nombre, " : ", piloto_segunda_posicion.tiempo_piloto, " sg y pertenece al equipo 1")
                beneficio_segunda_posición = (2000 + 0.10)
                print("El sueldo + beneficio por segunda posición para el piloto ", piloto_segunda_posicion.nombre, " del equipo 1 es de: ", beneficio_segunda_posición )
            print("El sueldo por segunda posición para el piloto ", piloto_segunda_posicion.nombre, " del equipo 1 es de: ", self.equipo1.sueldo_Piloto)
        elif self.equipo2.piloto1.nombre == piloto_segunda_posicion.nombre or self.equipo2.piloto2.nombre == piloto_segunda_posicion.nombre:
            if self.pista_seleccionada.tipo_exigencia_1 != piloto_segunda_posicion.bono_piloto and self.pista_seleccionada.tipo_exigencia_2 != piloto_segunda_posicion.bono_piloto:
                print("Segunda posición: ", piloto_segunda_posicion.nombre, " : ", piloto_segunda_posicion.tiempo_piloto, " sg y pertenece al equipo 2")
                beneficio_segunda_posición = (2000 + 0.10)
                print("El sueldo + beneficio por segunda posición para el piloto ", piloto_segunda_posicion.nombre, " del equipo 2 es de: ", beneficio_segunda_posición )
            print("El sueldo por segunda posición para el piloto ", piloto_segunda_posicion.nombre, " del equipo 2 es de: ", self.equipo2.sueldo_Piloto)
        
        
        
        
    # Calcular la nómina para los directores
    def calcular_nomina_directores(self):
        # Director equipo: 10% bono por pole position

        # Lista ordenada
        pole_position = ejecutar.calcular_pole_position()
        piloto_ganador = pole_position[0]
        

        if self.equipo1.piloto1.nombre == piloto_ganador.nombre or self.equipo1.piloto2.nombre == piloto_ganador.nombre:
            #print("GANADOR!: ", piloto_ganador.nombre, " : ", piloto_ganador.tiempo_piloto, " sg y pertenece al equipo equipo 1 ")
            beneficio_director = (4000 + 0.10)
            print("El sueldo + beneficio para el director ", directores[0], " del equipo 1 es de: ", beneficio_director)
        elif self.equipo2.piloto1.nombre == piloto_ganador.nombre or self.equipo2.piloto2.nombre == piloto_ganador.nombre:
            #print("GANADOR!: ", piloto_ganador.nombre, " : ", piloto_ganador.tiempo_piloto, " sg pertenece al equipo equipo 2 ")
            beneficio_director = (4000 + 0.10)
            print("El sueldo + beneficio para el director ", directores[1], " del equipo 2 es de: ", beneficio_director)
    

    # Calcular la nómina para los mecánicos
     # Mecánico: 5% extra si logra una parada en pits menor 2.2 segundos
    def calcular_nomina_mecanicos(self):
        print("metodo mecanicos")
        
        for i in (self.mecanicos):
            tiempo_total_mecanico = ejecutar.calcular_tiempo_pits()
            i.tiempo_mecanico = tiempo_total_mecanico
            
            if self.equipo1.mecanico1.nombre == i.nombre or self.equipo1.mecanico2.nombre == i.nombre or self.equipo1.mecanico3.nombre == i.nombre or self.equipo1.mecanico4.nombre == i.nombre:
                if i.tiempo_mecanico <= 2.2:
                    beneficio_mecanico = (3000 + 0.5)
                    print("El mecánico ", i.nombre, " que pertenece al equipo ", self.equipo1.nombre_Equipo," hizo un tiempo de: ", i.tiempo_mecanico, "El salario + beneficio es de: ", beneficio_mecanico)
                else:
                    print("El mecánico ", i.nombre, " que pertenece al equipo ", self.equipo1.nombre_Equipo," hizo un tiempo de: ", i.tiempo_mecanico, "El salario es de: ", 3000)
            elif self.equipo2.mecanico1.nombre == i.nombre or self.equipo2.mecanico2.nombre == i.nombre or self.equipo2.mecanico3.nombre == i.nombre or self.equipo2.mecanico4.nombre == i.nombre:
                if i.tiempo_mecanico <= 2.2:
                    beneficio_mecanico = (3000 + 0.5)
                    print("El mecánico ", i.nombre, " que pertenece al equipo ", self.equipo2.nombre_Equipo," hizo un tiempo de: ", i.tiempo_mecanico, "El salario + beneficio es de: ", beneficio_mecanico)
                else:
                    print("El mecánico ", i.nombre, " que pertenece al equipo ", self.equipo2.nombre_Equipo," hizo un tiempo de: ", i.tiempo_mecanico, "El salario es de: ", 3000)
                
       

ejecutar = Ejecutora()
# Lista ordenada
#pole_position = ejecutar.calcular_pole_position()
# Ver la pole position 
#for j in pole_position:
 #   print("Pole position: ", j.nombre, " es: ", j.tiempo_piloto)

nomina_primer_lugar = ejecutar.calcular_nomina_primer_lugar()
print("#########################################################################")
nomina_segundo_lugar = ejecutar.calcular_nomina_segundo_lugar()
print("#########################################################################")
nomina_director = ejecutar.calcular_nomina_directores()
print("#########################################################################")
nomina_mecanico = ejecutar.calcular_nomina_mecanicos()

