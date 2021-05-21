""" Ejercicio 1:
    Dado los 3 angulos de un trangulo definir que tipo de triangulo es.
"""

print("#################### TIPOS DE TRIÁNGULOS ##################")

angulo1 = int(input("Digite el primer angulo: "))
angulo2 = int(input("Digite el segundo angulo: "))
angulo3 = int(input("Digite el tercer angulo: "))

suma = angulo1 + angulo2 + angulo3

if suma == 90:
    print("Es un triángulo rectangulo")
elif suma < 90:
    print("Es un triángulo acutángulo")
elif suma > 90:
    print("Es un triángulo escaleno")
