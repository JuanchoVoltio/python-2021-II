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
    director = undefined
    mecanico1 = undefined
    mecanico2 = undefined
    mecanico3 = undefined
    mecanico4 = undefined
    piloto1 = undefined
    piloto2 = undefined

    # Definición del método constructor
    def __init__(self, director, mecanico1, mecanico2, mecanico3, mecanico4, piloto1, piloto2):
        self.director = director
        self.mecanico1 = mecanico1
        self.mecanico2 = mecanico2
        self.mecanico3 = mecanico3
        self.mecanico4 = mecanico4
        self.piloto1 = piloto1
        self.piloto2 = piloto2

class Piloto:
    nombre = undefined
    tiempo_piloto = undefined

    # Definición del método constructor
    def __init__(self, nombre):
        self.nombre = nombre



class Ejecutora:
    pista = []
    pilotos = []
    
    
    # Crear pilotos
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
    equipo1 = Equipo(directores[0],mecanicos[0],mecanicos[1],mecanicos[2],mecanicos[3],pilotos[0],pilotos[1])
    equipo2 = Equipo(directores[1],mecanicos[4],mecanicos[5],mecanicos[6],mecanicos[7],pilotos[2],pilotos[3])
    



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
        

ejecutar = Ejecutora()
# Lista ordenada
pole_position = ejecutar.calcular_pole_position()
# Ver la pole position 
for j in pole_position:
    print("Pole position: ", j.nombre, " es: ", j.tiempo_piloto)