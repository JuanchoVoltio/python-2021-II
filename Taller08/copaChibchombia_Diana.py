print("Fechas: habilitadas, inhabilitadas")
ingreso = input("¿Que tipo de fechas desea consultar?: ")


fechas_habilitadas = {
    'f1_enero': '23/01/2021', 'f2_enero': '31/01/2021',
    'f1_febrero': '01/02/2021', 'f2_febrero': '15/02/2021',
    'f1_marzo': '03/03/2021', 'f2_marzo': '21/03/2021',
    'f1_abril': '15/04/2021', 'f2_abril': '30/04/2021'
}

fechas_inhabilitadas = {
    'f1_enero': '01/01/2021', 'f2_enero': '15/01/2021',
    'f1_febrero': '25/02/2021', 'f2_febrero': '03/02/2021',
    'f1_marzo': '01/03/2021', 'f2_marzo': '28/03/2021',
    'f1_abril': '09/04/2021', 'f2_abril': '27/04/2021'
}

if ingreso == "habilitadas":
    print("=" * 30)
    print("Las fechas habilitadas son: ")
    print("=" * 30)
    for llave, valor in fechas_habilitadas.items():
        print(llave, " = ", valor)
elif ingreso == "inhabilitadas":
    print("=" * 30)
    print("Las fechas inhabilitadas son: ")
    print("=" * 30)
    for llave, valor in fechas_inhabilitadas.items():
        print(llave, " = ", valor)
else:
    print("Valor inexistente")