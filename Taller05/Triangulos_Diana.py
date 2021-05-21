""" Ejercicio 1:
    Dado los 3 angulos de un trangulo definir que tipo de triangulo es.
"""

print("#################### TIPOS DE TRIÁNGULOS ##################")

angulo1 = int(input("Digite el primer angulo: "))
angulo2 = int(input("Digite el segundo angulo: "))
angulo3 = int(input("Digite el tercer angulo: "))

if angulo1 and angulo2 and angulo3 > 0:
    suma = angulo1 + angulo2 + angulo3

if suma == 180:
    print("Inicia calculo")
elif angulo1 or angulo2 or angulo3 == 90:
    print("Es un triángulo rectángulo")
elif angulo1 or angulo2 or angulo3 < 90:
    print("Es un triángulo acutángulo")
elif angulo1 or angulo2 or angulo3 > 90:
    print("Es un triángulo escaleno")
else:
    print("Los valores no aplican")
