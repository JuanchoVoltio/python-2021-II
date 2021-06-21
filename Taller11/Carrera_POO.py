# Importo la librería random para utilizarlo en el cálculo del tiempo hecho por el piloto
import random

# Variable global
undefined = "Unknown"

# Definición de la clase piloto
class Piloto:
    # Definición de los atributos
    nombre = undefined
    apellido = undefined
    bono = undefined

    # Definición del método constructor
    def __init__(self, nombre, apellido, bono):
    
        self.nombre = nombre
        self.apellido = apellido
        self.bono = bono

    
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




class Carrera:
    # Definición de atributos
    pista = undefined
    pilotos = []

    # Definición del método constructor
    def __init__(self, pista, pilotos):
        self.pista = pista
        self.pilotos = pilotos
    
    #Retorna el tiempo del piloto
    def tiempo_piloto(self):
        for i in self.pilotos:
            total_tiempo = 0
            tiempo_piloto = random.randint(1,70)
            if i.bono == self.pista.tipo_exigencia_1 or i.bono == self.pista.tipo_exigencia_2:
                if i.bono == "Motor":
                    total_tiempo = (tiempo_piloto - 0.4)
                elif i.bono == "Chasis":
                    total_tiempo = (tiempo_piloto - 0.6)
                elif i.bono == "Aerodinámica":
                    total_tiempo = (tiempo_piloto - 0.5)
            else:
                total_tiempo = tiempo_piloto
            print("El tiempo del piloto ", i.nombre, i.apellido, " es: ", total_tiempo)



class Correr:
    # Definición de atributos
    pista = undefined
    pilotos = []
    carerera = undefined

    # Definición de los objetos de tipo Piloto
    piloto1 = Piloto("C.", "Muñoz","Chasis")
    pilotos.append(piloto1)

    piloto2 = Piloto("T.", "Kobayashi","Motor")
    pilotos.append(piloto2)

    piloto3 = Piloto("G.","Chavez", "Aerodinámica")
    pilotos.append(piloto3)

    piloto4 = Piloto("P.","Wherlein","Motor")
    pilotos.append(piloto4)

    piloto5 = Piloto("D.", "Ricciardo", "Chasis")
    pilotos.append(piloto5)

    # Definición de los objetos de tipo PiSTA
    pista1 = Pista("Long Beach","Chasis","Aerodinámica")
    pista2 = Pista("Interlagos","Motor","Chasis")
    pista3 = Pista("Suzuka","Aerodinámica", "Chasis")
    pista4 = Pista("Silverstone","Motor","Aerodinámica")

    mensaje = input("¿Que pista desea consultar?: ")

    if mensaje == "Long Beach":
        # Creación de carrera
        carrera1 = Carrera(pista1,pilotos)
        carrera1.tiempo_piloto()
    elif mensaje == "Interlagos":
        carrera2 = Carrera(pista2, pilotos)
        carrera2.tiempo_piloto()
    elif mensaje == "Suzuka":
        carrera3 = Carrera(pista3, pilotos)
        carrera3.tiempo_piloto()
    elif mensaje == "Silverstone":
        carrera4 = Carrera(pista4, pilotos)
        carrera4.tiempo_piloto()
    else:
        print("Pista no existe.")
