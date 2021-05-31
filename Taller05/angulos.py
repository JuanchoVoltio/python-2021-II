#angulos de triangulos


angulo_1=int(input ("digite un numero:  "))
angulo_2=int(input ("digite un numero:  "))
angulo_3=int(input ("digite un numero:  "))

numero   = angulo_1+angulo_2+angulo_3          

if numero==180:

    if (angulo_1==angulo_2==angulo_3):
             print ("Es un Triangulo Equilatero")
    elif (angulo_1==angulo_2 or  angulo_1==angulo_3  or angulo_2==angulo_3):
        print ("Es un Triangulo Is'oceles")
    else:
        print ("Es un Triangulo Escaleno")
    

else:
    print ("los angulos no corresponde a un triangulo")
