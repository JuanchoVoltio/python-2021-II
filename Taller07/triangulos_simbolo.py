#formas con *


#opcion A
a=int(input("Ingrese  el alto del rectangulo:  "))
a_1=int(input("Ingrese  el ancho del rectangulo:  "))

for i in range(1,a+1):
    for i_1 in range(1,a_1+1):
            print("*",end=" ")
    print(" ")
        
        
           

            
#opcion B
b=int(input("Ingrese la altura del triangulo:  "))

for i in range(b+1):
    print("*"*i)


    

#opcion C
c=int(input("Ingrese  la altura del triangulo:  "))

for i in range(c):
    espacio_b= c - i -1
    simbolo = 1 + i * 2
    print(" " * espacio_b + "*" * simbolo)
    

#opcion D
d=int(input("Ingrese  la altura del triangulo:  "))

for i in range (d,0,-1):
    for i_1 in range (d,i,1):
        print ("*",end ="")

