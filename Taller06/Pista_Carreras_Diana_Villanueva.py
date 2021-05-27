# Importo la librería random para utilizarlo en el calculo del tiempo hecho por el piloto
import random

# Definición de las listas y tuplas
bonus_tag = ("chasis","motor","aerodinamica")
pilotos = ["C. Muñoz", "Kobayashi", "G. Chavez", "P. Wherlein", "D. Riccardo"]
bonus_piloto = [bonus_tag[0],bonus_tag[1], bonus_tag[2], bonus_tag[1], bonus_tag[0]]
pistas = ("Long Beach", "Interlagos", "Suzuka", "Silverstone")

solicitar_pista = input("¿Que pista correrán los pilotos?: ")

# Si la pista es Long Beach
if solicitar_pista == pistas[0]:
    # Bonos asociados a a la pista Long Beach
    bono1_Long_Beach = [bonus_tag[0]]
    bono2_Long_Beach = [bonus_tag[2]]

    # Calculo del tiempo para el piloto Muñoz
    tiempo_Munoz = random.randint(1,70)
    # Asocio el piloto al bono que le pertenece
    bono_Munoz = [bonus_tag[0]]

    # Calculo del tiempo para el piloto Kobayashi
    tiempo_Kobayashi = random.randint(1,70)
    # Asocio el piloto al bono que le pertenece
    bono_Kobayashi = [bonus_tag[1]]

    # Calculo del tiempo para el piloto Chavez
    tiempo_Chavez = random.randint(1,70)
    # Asocio el piloto al bono que le pertenece
    bono_Chavez = [bonus_tag[2]]

    # Calculo del tiempo para el piloto Wherlein
    tiempo_Wherlein = random.randint(1,70)
    # Asocio el piloto al bono que le pertenece
    bono_Wherlein = [bonus_tag[1]]

    # Calculo del tiempo para el piloto Riccardo
    tiempo_Ricciardo = random.randint(1,70)
    # Asocio el piloto al bono que le pertenece
    bono_Ricciardo = [bonus_tag[0]]

    # Comparamos si el bono del piloto es equivalente al bono de la pista entonces restará el valor correspondiente al tiempo hecho por el usuario
    if bono1_Long_Beach == bono_Munoz or bono2_Long_Beach == bono_Munoz:
        tiempo_total_Munoz = (tiempo_Munoz - 0.6)
    else: # Si no aplica entonces no le resta ningun valor al tiempo hecho por el piloto
        tiempo_total_Munoz = tiempo_Munoz
    if bono1_Long_Beach == bono_Kobayashi or bono2_Long_Beach == bono_Kobayashi:
        tiempo_total_Kobayashi = (tiempo_Kobayashi - 0.4)
    else:
        tiempo_total_Kobayashi = tiempo_Kobayashi
    if bono1_Long_Beach == bono_Chavez or bono2_Long_Beach == bono_Chavez:
        tiempo_total_Chavez = (tiempo_Chavez - 0.5)
    else:
        tiempo_total_Chavez = tiempo_Chavez
    if bono1_Long_Beach == bono_Wherlein or bono2_Long_Beach == bono_Wherlein:
        tiempo_total_Wherlein = (tiempo_Wherlein - 0.4)
    else:
        tiempo_total_Wherlein = tiempo_Wherlein
    if bono1_Long_Beach == bono_Ricciardo or bono2_Long_Beach == bono_Ricciardo:
        tiempo_total_Ricciardo = (tiempo_Ricciardo - 0.6)
    else:
        tiempo_total_Ricciardo = tiempo_Ricciardo

    
    # Prueba de escritorio
    """print("El tiempo de Muñoz fue: " + str(tiempo_Munoz) + " - bono: " + str(tiempo_total_Munoz) + " el bono asociado al piloto es: " + str(bono_Munoz) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Kobayashi fue: " + str(tiempo_Kobayashi) + " - bono: " + str(tiempo_total_Kobayashi) + " el bono asociado al piloto es: " + str(bono_Kobayashi) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Chavez fue: " + str(tiempo_Chavez) + " - bono: " + str(tiempo_total_Chavez) + " el bono asociado al piloto es: " + str(bono_Chavez) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Wherlein fue: " + str(tiempo_Wherlein) + " - bono: " + str(tiempo_total_Wherlein) + " el bono asociado al piloto es: " + str(bono_Wherlein) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Ricciardo fue: " + str(tiempo_Ricciardo) + " - bono: " + str(tiempo_total_Ricciardo) + " el bono asociado al piloto es: " + str(bono_Ricciardo) + " la pista que corrió fue: " + solicitar_pista)"""

    # Clasificación de la carrera
    print("##########################################################")
    print("             PISTA LONG BEACH")
    print("#########################################################")
    print("     Piloto" +   "     |" + "      Tiempo Total")
    print("#########################################################")
    print(pilotos[0] + "        |" + "      "+ str(round(tiempo_total_Munoz,2)))
    print(pilotos[1] + "       |" + "      " + str(round(tiempo_total_Kobayashi,2)))
    print(pilotos[2] + "       |" + "      " + str(round(tiempo_total_Chavez,2)))
    print(pilotos[3] + "     |" + "      " + str(round(tiempo_total_Wherlein,2)))
    print(pilotos[4] + "     |" + "      " + str(round(tiempo_total_Ricciardo,2)))
    
# Si la pista es Interlagos
elif solicitar_pista == pistas[1]:
    # Bonos asociados a a la pista Long Beach
    bono1_Interlagos = [bonus_tag[1]]
    bono2_Interlagos = [bonus_tag[0]]

    # Calculo del tiempo para el piloto Muñoz
    tiempo_Munoz = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Munoz = [bonus_tag[0]]

    # Calculo del tiempo para el piloto Kobayashi
    tiempo_Kobayashi = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Kobayashi = [bonus_tag[1]]

    # Calculo del tiempo para el piloto Chavez
    tiempo_Chavez = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Chavez = [bonus_tag[2]]

    # Calculo del tiempo para el piloto Wherlein
    tiempo_Wherlein = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Wherlein = [bonus_tag[1]]

    # Calculo del tiempo para el piloto Riccardo
    tiempo_Ricciardo = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Ricciardo = [bonus_tag[0]]

    # Comparamos si el bono del piloto es equivalente al bono de la pista entonces restará el valor correspondiente al tiempo hecho por el usuario
    if bono1_Interlagos == bono_Munoz or bono2_Interlagos == bono_Munoz:
        tiempo_total_Munoz = (tiempo_Munoz - 0.6) # Si no aplica entonces no le resta ningun valor al tiempo hecho por el piloto
    else: 
        tiempo_total_Munoz = tiempo_Munoz
    if bono1_Interlagos == bono_Kobayashi or bono2_Interlagos == bono_Kobayashi:
        tiempo_total_Kobayashi = (tiempo_Kobayashi - 0.4)
    else:
        tiempo_total_Kobayashi = tiempo_Kobayashi
    if bono1_Interlagos == bono_Chavez or bono2_Interlagos == bono_Chavez:
        tiempo_total_Chavez = (tiempo_Chavez - 0.5)
    else:
        tiempo_total_Chavez = tiempo_Chavez
    if bono1_Interlagos == bono_Wherlein or bono2_Interlagos == bono_Wherlein:
        tiempo_total_Wherlein = (tiempo_Wherlein - 0.4)
    else:
        tiempo_total_Wherlein = tiempo_Wherlein
    if bono1_Interlagos == bono_Ricciardo or bono2_Interlagos == bono_Ricciardo:
        tiempo_total_Ricciardo = (tiempo_Ricciardo - 0.6)
    else:
        tiempo_total_Ricciardo = tiempo_Ricciardo

    # Prueba de escritorio
    """print("El tiempo de Muñoz fue: " + str(tiempo_Munoz) + " - bono: " + str(tiempo_total_Munoz) + " el bono asociado al piloto es: " + str(bono_Munoz) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Kobayashi fue: " + str(tiempo_Kobayashi) + " - bono: " + str(tiempo_total_Kobayashi) + " el bono asociado al piloto es: " + str(bono_Kobayashi) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Chavez fue: " + str(tiempo_Chavez) + " - bono: " + str(tiempo_total_Chavez) + " el bono asociado al piloto es: " + str(bono_Chavez) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Wherlein fue: " + str(tiempo_Wherlein) + " - bono: " + str(tiempo_total_Wherlein) + " el bono asociado al piloto es: " + str(bono_Wherlein) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Ricciardo fue: " + str(tiempo_Ricciardo) + " - bono: " + str(tiempo_total_Ricciardo) + " el bono asociado al piloto es: " + str(bono_Ricciardo) + " la pista que corrió fue: " + solicitar_pista)"""

    # Clasificación de la carrera
    print("##########################################################")
    print("             PISTA INTERLAGOS")
    print("#########################################################")
    print("     Piloto" +   "     |" + "      Tiempo Total")
    print("#########################################################")
    print(pilotos[0] + "        |" + "      "+ str(round(tiempo_total_Munoz,2)))
    print(pilotos[1] + "       |" + "      " + str(round(tiempo_total_Kobayashi,2)))
    print(pilotos[2] + "       |" + "      " + str(round(tiempo_total_Chavez,2)))
    print(pilotos[3] + "     |" + "      " + str(round(tiempo_total_Wherlein,2)))
    print(pilotos[4] + "     |" + "      " + str(round(tiempo_total_Ricciardo,2)))

# Si la pista es Suzuka
elif solicitar_pista == pistas[2]:
    # Bonos asociados a a la pista Long Beach
    bono1_Suzuka = [bonus_tag[2]]
    bono2_Suzuka = [bonus_tag[0]]

    # Calculo del tiempo para el piloto Muñoz
    tiempo_Munoz = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Munoz = [bonus_tag[0]]

    # Calculo del tiempo para el piloto Kobayashi
    tiempo_Kobayashi = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Kobayashi = [bonus_tag[1]]

    # Calculo del tiempo para el piloto Chavez
    tiempo_Chavez = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Chavez = [bonus_tag[2]]

    # Calculo del tiempo para el piloto Wherlein
    tiempo_Wherlein = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Wherlein = [bonus_tag[1]]

    # Calculo del tiempo para el piloto Riccardo
    tiempo_Ricciardo = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Ricciardo = [bonus_tag[0]]

    # Comparamos si el bono del piloto es equivalente al bono de la pista entonces restará el valor correspondiente al tiempo hecho por el usuario
    if bono1_Suzuka == bono_Munoz or bono2_Suzuka == bono_Munoz:
        tiempo_total_Munoz = (tiempo_Munoz - 0.6) # Si no aplica entonces no le resta ningun valor al tiempo hecho por el piloto    
    else: 
        tiempo_total_Munoz = tiempo_Munoz
    if bono1_Suzuka == bono_Kobayashi or bono2_Suzuka == bono_Kobayashi:
        tiempo_total_Kobayashi = (tiempo_Kobayashi - 0.4)
    else:
        tiempo_total_Kobayashi = tiempo_Kobayashi
    if bono1_Suzuka == bono_Chavez or bono2_Suzuka == bono_Chavez:
        tiempo_total_Chavez = (tiempo_Chavez - 0.5)
    else:
        tiempo_total_Chavez = tiempo_Chavez
    if bono1_Suzuka == bono_Wherlein or bono2_Suzuka == bono_Wherlein:
        tiempo_total_Wherlein = (tiempo_Wherlein - 0.4)
    else:
        tiempo_total_Wherlein = tiempo_Wherlein
    if bono1_Suzuka == bono_Ricciardo or bono2_Suzuka == bono_Ricciardo:
        tiempo_total_Ricciardo = (tiempo_Ricciardo - 0.6)
    else:
        tiempo_total_Ricciardo = tiempo_Ricciardo

    # Prueba de escritorio
    """print("El tiempo de Muñoz fue: " + str(tiempo_Munoz) + " - bono: " + str(tiempo_total_Munoz) + " el bono asociado al piloto es: " + str(bono_Munoz) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Kobayashi fue: " + str(tiempo_Kobayashi) + " - bono: " + str(tiempo_total_Kobayashi) + " el bono asociado al piloto es: " + str(bono_Kobayashi) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Chavez fue: " + str(tiempo_Chavez) + " - bono: " + str(tiempo_total_Chavez) + " el bono asociado al piloto es: " + str(bono_Chavez) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Wherlein fue: " + str(tiempo_Wherlein) + " - bono: " + str(tiempo_total_Wherlein) + " el bono asociado al piloto es: " + str(bono_Wherlein) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Ricciardo fue: " + str(tiempo_Ricciardo) + " - bono: " + str(tiempo_total_Ricciardo) + " el bono asociado al piloto es: " + str(bono_Ricciardo) + " la pista que corrió fue: " + solicitar_pista)"""

    # Clasificación de la carrera
    print("##########################################################")
    print("             PISTA SUZUKA")
    print("#########################################################")
    print("     Piloto" +   "     |" + "      Tiempo Total")
    print("#########################################################")
    print(pilotos[0] + "        |" + "      "+ str(round(tiempo_total_Munoz,2)))
    print(pilotos[1] + "       |" + "      " + str(round(tiempo_total_Kobayashi,2)))
    print(pilotos[2] + "       |" + "      " + str(round(tiempo_total_Chavez,2)))
    print(pilotos[3] + "     |" + "      " + str(round(tiempo_total_Wherlein,2)))
    print(pilotos[4] + "     |" + "      " + str(round(tiempo_total_Ricciardo,2)))

# Si la pista es Interlagos
elif solicitar_pista == pistas[1]:
    # Bonos asociados a a la pista Long Beach
    bono1_Interlagos = [bonus_tag[1]]
    bono2_Interlagos = [bonus_tag[0]]

    # Calculo del tiempo para el piloto Muñoz
    tiempo_Munoz = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Munoz = [bonus_tag[0]]

    # Calculo del tiempo para el piloto Kobayashi
    tiempo_Kobayashi = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Kobayashi = [bonus_tag[1]]

    # Calculo del tiempo para el piloto Chavez
    tiempo_Chavez = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Chavez = [bonus_tag[2]]

    # Calculo del tiempo para el piloto Wherlein
    tiempo_Wherlein = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Wherlein = [bonus_tag[1]]

    # Calculo del tiempo para el piloto Riccardo
    tiempo_Ricciardo = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Ricciardo = [bonus_tag[0]]

    # Comparamos si el bono del piloto es equivalente al bono de la pista entonces restará el valor correspondiente al tiempo hecho por el usuario
    if bono1_Interlagos == bono_Munoz or bono2_Interlagos == bono_Munoz:
        tiempo_total_Munoz = (tiempo_Munoz - 0.6) # Si no aplica entonces no le resta ningun valor al tiempo hecho por el piloto
    else: 
        tiempo_total_Munoz = tiempo_Munoz
    if bono1_Interlagos == bono_Kobayashi or bono2_Interlagos == bono_Kobayashi:
        tiempo_total_Kobayashi = (tiempo_Kobayashi - 0.4)
    else:
        tiempo_total_Kobayashi = tiempo_Kobayashi
    if bono1_Interlagos == bono_Chavez or bono2_Interlagos == bono_Chavez:
        tiempo_total_Chavez = (tiempo_Chavez - 0.5)
    else:
        tiempo_total_Chavez = tiempo_Chavez
    if bono1_Interlagos == bono_Wherlein or bono2_Interlagos == bono_Wherlein:
        tiempo_total_Wherlein = (tiempo_Wherlein - 0.4)
    else:
        tiempo_total_Wherlein = tiempo_Wherlein
    if bono1_Interlagos == bono_Ricciardo or bono2_Interlagos == bono_Ricciardo:
        tiempo_total_Ricciardo = (tiempo_Ricciardo - 0.6)
    else:
        tiempo_total_Ricciardo = tiempo_Ricciardo
    
    # Prueba de escritorio
    """print("El tiempo de Muñoz fue: " + str(tiempo_Munoz) + " - bono: " + str(tiempo_total_Munoz) + " el bono asociado al piloto es: " + str(bono_Munoz) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Kobayashi fue: " + str(tiempo_Kobayashi) + " - bono: " + str(tiempo_total_Kobayashi) + " el bono asociado al piloto es: " + str(bono_Kobayashi) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Chavez fue: " + str(tiempo_Chavez) + " - bono: " + str(tiempo_total_Chavez) + " el bono asociado al piloto es: " + str(bono_Chavez) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Wherlein fue: " + str(tiempo_Wherlein) + " - bono: " + str(tiempo_total_Wherlein) + " el bono asociado al piloto es: " + str(bono_Wherlein) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Ricciardo fue: " + str(tiempo_Ricciardo) + " - bono: " + str(tiempo_total_Ricciardo) + " el bono asociado al piloto es: " + str(bono_Ricciardo) + " la pista que corrió fue: " + solicitar_pista)"""

    # Clasificación de la carrera
    print("##########################################################")
    print("             PISTA INTERLAGOS")
    print("#########################################################")
    print("     Piloto" +   "     |" + "      Tiempo Total")
    print("#########################################################")
    print(pilotos[0] + "        |" + "      "+ str(round(tiempo_total_Munoz,2)))
    print(pilotos[1] + "       |" + "      " + str(round(tiempo_total_Kobayashi,2)))
    print(pilotos[2] + "       |" + "      " + str(round(tiempo_total_Chavez,2)))
    print(pilotos[3] + "     |" + "      " + str(round(tiempo_total_Wherlein,2)))
    print(pilotos[4] + "     |" + "      " + str(round(tiempo_total_Ricciardo,2)))

# Si la pista es Silverstone
elif solicitar_pista == pistas[3]:
    # Bonos asociados a a la pista Long Beach
    bono1_Silverstone = [bonus_tag[1]]
    bono2_Silverstone = [bonus_tag[2]]

    # Calculo del tiempo para el piloto Muñoz
    tiempo_Munoz = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Munoz = [bonus_tag[0]]

    # Calculo del tiempo para el piloto Kobayashi
    tiempo_Kobayashi = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Kobayashi = [bonus_tag[1]]

    # Calculo del tiempo para el piloto Chavez
    tiempo_Chavez = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Chavez = [bonus_tag[2]]

    # Calculo del tiempo para el piloto Wherlein
    tiempo_Wherlein = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Wherlein = [bonus_tag[1]]

    # Calculo del tiempo para el piloto Riccardo
    tiempo_Ricciardo = random.randint(1,70)/10
    # Asocio el piloto al bono que le pertenece
    bono_Ricciardo = [bonus_tag[0]]

    # Comparamos si el bono del piloto es equivalente al bono de la pista entonces restará el valor correspondiente al tiempo hecho por el usuario
    if bono1_Silverstone == bono_Munoz or bono2_Silverstone == bono_Munoz:
        tiempo_total_Munoz = (tiempo_Munoz - 0.6) # Si no aplica entonces no le resta ningun valor al tiempo hecho por el piloto
    else: 
        tiempo_total_Munoz = tiempo_Munoz
    if bono1_Silverstone == bono_Kobayashi or bono2_Silverstone == bono_Kobayashi:
        tiempo_total_Kobayashi = (tiempo_Kobayashi - 0.4)
    else:
        tiempo_total_Kobayashi = tiempo_Kobayashi
    if bono1_Silverstone == bono_Chavez or bono2_Silverstone == bono_Chavez:
        tiempo_total_Chavez = (tiempo_Chavez - 0.5)
    else:
        tiempo_total_Chavez = tiempo_Chavez
    if bono1_Silverstone == bono_Wherlein or bono2_Silverstone == bono_Wherlein:
        tiempo_total_Wherlein = (tiempo_Wherlein - 0.4)
    else:
        tiempo_total_Wherlein = tiempo_Wherlein
    if bono1_Silverstone == bono_Ricciardo or bono2_Silverstone == bono_Ricciardo:
        tiempo_total_Ricciardo = (tiempo_Ricciardo - 0.6)
    else:
        tiempo_total_Ricciardo = tiempo_Ricciardo
    
    # Prueba de escritorio
    """print("El tiempo de Muñoz fue: " + str(tiempo_Munoz) + " - bono: " + str(tiempo_total_Munoz) + " el bono asociado al piloto es: " + str(bono_Munoz) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Kobayashi fue: " + str(tiempo_Kobayashi) + " - bono: " + str(tiempo_total_Kobayashi) + " el bono asociado al piloto es: " + str(bono_Kobayashi) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Chavez fue: " + str(tiempo_Chavez) + " - bono: " + str(tiempo_total_Chavez) + " el bono asociado al piloto es: " + str(bono_Chavez) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Wherlein fue: " + str(tiempo_Wherlein) + " - bono: " + str(tiempo_total_Wherlein) + " el bono asociado al piloto es: " + str(bono_Wherlein) + " la pista que corrió fue: " + solicitar_pista)
    print("El tiempo de Ricciardo fue: " + str(tiempo_Ricciardo) + " - bono: " + str(tiempo_total_Ricciardo) + " el bono asociado al piloto es: " + str(bono_Ricciardo) + " la pista que corrió fue: " + solicitar_pista)"""

    # Clasificación de la carrera
    print("##########################################################")
    print("             PISTA SILVERSTONE")
    print("#########################################################")
    print("     Piloto" +   "     |" + "      Tiempo Total")
    print("#########################################################")
    print(pilotos[0] + "        |" + "      "+ str(round(tiempo_total_Munoz,2)))
    print(pilotos[1] + "       |" + "      " + str(round(tiempo_total_Kobayashi,2)))
    print(pilotos[2] + "       |" + "      " + str(round(tiempo_total_Chavez,2)))
    print(pilotos[3] + "     |" + "      " + str(round(tiempo_total_Wherlein,2)))
    print(pilotos[4] + "     |" + "      " + str(round(tiempo_total_Ricciardo,2)))

