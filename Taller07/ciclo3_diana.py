h = int(input("filas: "))
b = int(input("Columnas: "))

for i in range(h,0,-1):
    #(h-i) = Indica cuantos espacios quiero que tenga la fila
    # * (b) = Indica las columnas que quiero que tenga cada fila
    print(" "*(h-i)+"*"*(b))
    b = b - 2 # Se le resta 2 para mostrar la figura
