import director
import piloto
import mecanico
import pista

class Datos:

    pilotos = []
    directores = []
    mecanicos = []
    pistas = []
    bonos = ["chasis","motor","aerodinamica"]

    def obtener_Piloto(self):
        # Creación de los piltos
        self.pilotos.append(piloto.Piloto("C. Muñoz",3000,self.bonos[0],"Equipo 1"))
        self.pilotos.append(piloto.Piloto("Kobayashi",3000,self.bonos[1],"Equipo 1"))
        self.pilotos.append(piloto.Piloto("G. Chavez",3000,self.bonos[2],"Equipo 2"))
        self.pilotos.append(piloto.Piloto("P. Wherlein",3000,self.bonos[1],"Equipo 2"))
        return self.pilotos
    

    def obtener_Director(self):
        # Creacion de los directores
        self.directores.append(director.Director("J. Montoya", 4000,"Equipo 1"))
        self.directores.append(director.Director("T. Asprilla", 4000,"Equipo 2"))
        return self.directores
    

    def obtener_Mecanico(self):
        # Creación de los mecánicos
        self.mecanicos.append(mecanico.Mecanico("Chavez", 2000,"Equipo 1"))
        self.mecanicos.append(mecanico.Mecanico("Villanueva", 2000,"Equipo 1"))
        self.mecanicos.append(mecanico.Mecanico("Ramirez", 2000,"Equipo 1"))
        self.mecanicos.append(mecanico.Mecanico("Duque", 2000,"Equipo 1"))
        self.mecanicos.append(mecanico.Mecanico("Henao", 2000,"Equipo 2"))
        self.mecanicos.append(mecanico.Mecanico("Quintero", 2000,"Equipo 2"))
        self.mecanicos.append(mecanico.Mecanico("Avellaneda", 2000,"Equipo 2"))
        self.mecanicos.append(mecanico.Mecanico("Ortiz", 2000,"Equipo 2"))
        return self.mecanicos


    def obtener_Pistas(self):
        # Creación de las pistas
        self.pistas.append(pista.Pista("Long Beach",self.bonos[0],self.bonos[2]))
        self.pistas.append(pista.Pista("Interlagos",self.bonos[1],self.bonos[0]))
        self.pistas.append(pista.Pista("Suzuka",self.bonos[2],self.bonos[0]))
        self.pistas.append(pista.Pista("Silverstone",self.bonos[1],self.bonos[2]))
        return self.pistas
