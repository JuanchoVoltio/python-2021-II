# Importo la librería random para utilizarlo en el cálculo del tiempo hecho por el piloto
from math import pi
import random

# Variable global
undefined = "Unknown"



bono = ["chasis","motor","aerodinamica"]
pilotos = []
pistas = ["Long Beach", "Interlagos", "Suzuka", "Silverstone"]
directores = ["J. Montoya", "T, Aprilla"]
mecanicos = ["Chavez", "Villanueva", "Ramirez", "Duque", "Henao", "Quintero", "Avellaneda", "Ortiz"]
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

    # Definición del método constructor
    def __init__(self, nombre):
        self.nombre = nombre



class Ejecutora:
    pista = []
    pilotos = []
    sueldos = []
    nombre_Equipos = []
    
    
    # Crear pilotos y agregarlos al arreglo vacío
    piloto1 = Piloto("C. Muñoz")
    piloto2 = Piloto("Kobayashi")
    piloto3 = Piloto("G. Chavez")
    piloto4 = Piloto("P. Wherlein")
    piloto5= Piloto("D. Riccardo")

    pilotos.append(piloto1)
    pilotos.append(piloto2)
    pilotos.append(piloto3)
    pilotos.append(piloto4)
    pilotos.append(piloto5)

    #Crear pistas con sus respectivas exigencias  
    pista1 = Pista(pistas[0],bono[0], bono[2])
    pista2 = Pista(pistas[1],bono[1],bono[0])
    pista3 = Pista(pistas[2],bono[2],bono[0])
    pista4 = Pista(pistas[3],bono[1],bono[2])

   
    
    #Crear equipos
    equipo1 = Equipo("Equipo 1",directores[0],mecanicos[0],mecanicos[1],mecanicos[2],mecanicos[3],pilotos[0],pilotos[1],4000,3000,2000)
    equipo2 = Equipo("Equipo 2",directores[1],mecanicos[4],mecanicos[5],mecanicos[6],mecanicos[7],pilotos[2],pilotos[3],4000,3000,200)
    



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
        
    # Calcular la nómina
    def calcular_nomina(self):
        # Director equipo: 10% bono por pole position

        # Lista ordenada
        pole_position = ejecutar.calcular_pole_position()
        """print("####################### POLE POSITION ################################")
        for j in pole_position:
            # Si el piloto 1 o piloto 2 son iguales al nombre que itera entonces
            if self.equipo1.piloto1.nombre == j.nombre or self.equipo1.piloto2.nombre == j.nombre:
                print(j.nombre, " es: ", j.tiempo_piloto, " pertenece al equipo equipo 1 ")
            elif self.equipo2.piloto1.nombre == j.nombre or self.equipo2.piloto2.nombre == j.nombre:
                print(j.nombre, " es: ", j.tiempo_piloto, " pertenece al equipo equipo 2 ")"""
        
        piloto_ganador = pole_position[0]

        if self.equipo1.piloto1.nombre == piloto_ganador.nombre or self.equipo1.piloto2.nombre == piloto_ganador.nombre:
            print("GANADOR!: ", piloto_ganador.nombre, " : ", piloto_ganador.tiempo_piloto, " sg y pertenece al equipo equipo 1 ")
            beneficio_director = (4000 + 0.10)
            print("El suelto + beneficio para el director ", directores[0], " del equipo 1 es de: ", beneficio_director)
        elif self.equipo2.piloto1.nombre == piloto_ganador.nombre or self.equipo2.piloto2.nombre == piloto_ganador.nombre:
            print("GANADOR!: ", piloto_ganador.nombre, " : ", piloto_ganador.tiempo_piloto, " sg pertenece al equipo equipo 2 ")
            beneficio_director = (4000 + 0.10)
            print("El suelto + beneficio para el director ", directores[1], " del equipo 2 es de: ", beneficio_director)

        # Piloto: 10% extra si clasifica 2do o mejor
        #         20% si lo hace en una pista donde no tiene bono


        # Mecánico: 5% extra si logra una parada en pits menor 2.2 segundos



            

ejecutar = Ejecutora()
# Lista ordenada
#pole_position = ejecutar.calcular_pole_position()
# Ver la pole position 
#for j in pole_position:
 #   print("Pole position: ", j.nombre, " es: ", j.tiempo_piloto)

pole = ejecutar.calcular_nomina()