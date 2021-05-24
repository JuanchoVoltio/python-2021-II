'''formula_1'''

import random

Tiempo_Rueda1 = random.randint(0,15)/10
Tiempo_Rueda2 = random.randint(0,15)/10
Tiempo_Rueda3 = random.randint(0,15)/10
Tiempo_Rueda4 = random.randint(0,15)/10

Tiempo_general = (Tiempo_Rueda1+Tiempo_Rueda2+Tiempo_Rueda3+Tiempo_Rueda4)

Rueda1 = " Para la Rueda 1 {1} {0} segundos"
Rueda2 = " Para la Rueda 2 {1} {0} segundos"
Rueda3 = " Para la Rueda 3 {1} {0} segundos"
Rueda4 = " Para la Rueda 4 {1} {0} segundos"

Proceso = """El vehiculo entra al bloque y los mecanicos se dividen en cuatro grupos, de forma que mietras uno quita una rueda el otro la pone,
terminando el cambio de ruedas el vehiculo retoma la carrera.\n"""

Tiempo_cambio_ruedas = Tiempo_general

print ("En una parada de pits existe un vehiculo, bloque respectivo y 8 mecanicos si quiere saber como opera presione enter")

input(),print (Proceso)


print ("""Si desea saber el timpo gastado por los mecanicos en cambiar las ruedas presione enter nuevamente.\nNOTA: tenga en cuenta que el tiempo puede variar, dependiendo de la agilidad de los mecanicos """)

input ()
print ("El tiempo gastado fue de:",Tiempo_cambio_ruedas,"segundos")
print ("Para mas detalle presione enter ")

input ()

print (Rueda1.format(Tiempo_Rueda1,"tardaron"))
print (Rueda2.format(Tiempo_Rueda2,"tardaron"))
print (Rueda3.format(Tiempo_Rueda3,"tardaron"))
print (Rueda4.format(Tiempo_Rueda4,"tardaron"))











