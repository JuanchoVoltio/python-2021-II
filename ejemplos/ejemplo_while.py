'''pregunta_inicial = "¿Por qué las aves vuelan? "
respuesta = input(pregunta_inicial)


while respuesta != "porque si":
    respuesta = input("¿Por qué? ")

print("El niño se quedó dormido....")'''


age = int(input("¿Cuál es edad? "))
city = input("¿De dónde eres? ")
level = input("¿Cuál es su estrato? ")

person_found = (age >= 18 and city == "Santa Marta" and level == '3')


while not person_found:
    print('-' * 10)
    age = int(input("¿Cuál es edad? "))
    if age < 18:
        break
    
    city = input("¿De dónde eres? ")
    level = input("¿Cuál es su estrato? ")

    person_found = (age >= 18 and city == "Santa Marta" and level == '3')

else:
    print("Persona encontrada: ", person_found)


#End of program
