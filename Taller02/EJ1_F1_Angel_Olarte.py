'''formula_1'''

import random

Proceso = """El vehiculo entre al bloque y los mecanicos se dividen en cuatro grupos,

de forma que mietras uno quita una rueda el otro la pone,

terminando el cambio de ruedas el vehiculo retoma la carrera"""

Tiempo_cambio_ruedas = random.randint(2,5)

print ("""En una parada de pits existe un vehiculo, bloque respectivo y 8 mecanicos

                              si quiere saber como opera digite si""")
input ()

print (Proceso)
print ()

print ("""Si desea saber el timpo gastado por los mecanicos en cambiar las ruedas
                                      digite si nuevamente""")

input ()

print ("El tiempo gastado fue de:",Tiempo_cambio_ruedas,"segundos")











