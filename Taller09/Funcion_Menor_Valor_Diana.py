# Crear un procedimiento que encuentre el menor valor en una colección de números.

#definimos una lista vacia
lista=[]
#disponemos un ciclo de 5 vueltas
for x in range(5):
    valor=int(input("Ingrese 5 valores enteros: "))
    lista.append(valor)
#imprimimos la lista    
print("La lista se llenó con: " + str(lista))


def encontrarMenorValor(mi_lista):
    temporal = min(mi_lista)
    return temporal

resultado = encontrarMenorValor(lista)
print("El menor valor es: " + str(resultado))