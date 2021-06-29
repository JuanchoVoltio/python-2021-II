import random
import datos

class Simuladores:

    mi_dato = datos.Datos()
    pilotos = mi_dato.obtener_Piloto()

#Retorna el tiempo del piloto
    def calcular_pole_position(self):
        
        # Recorrer el listado de pilotos
        for i in self.pilotos:
            # Calcular el tiempo por medio de este random
            tiempo_piloto = random.randint(1,70)
            # A cada piloto le guardo el tiempo que obtuvo
            i.tiempo_piloto = tiempo_piloto
        
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

        

