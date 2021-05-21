""" Ejercicio 1:
    Dado los 3 ángulos de un triángulo definir que tipo de triángulo es.
"""

print("#################### TIPOS DE TRIÁNGULOS ##################")

angulo1 = int(input("Digite el primer ángulo: "))
angulo2 = int(input("Digite el segundo ángulo: "))
angulo3 = int(input("Digite el tercer ángulo: "))

if angulo1 > 0 and angulo2 > 0 and angulo3 > 0:
    suma = angulo1 + angulo2 + angulo3
    if suma == 180 and angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("Es un triángulo rectángulo")
    elif suma == 180 and angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        print("Es un triángulo acutángulo")
    elif suma == 180 and angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print("Es un triángulo escaleno")
    else:
        print("Los ángulos no corresponden a un triángulo (La suma de estos debe ser mayor que 180)")
else:
    print("Los valores no aplican")
