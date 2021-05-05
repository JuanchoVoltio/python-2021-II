import random 

template_mecanicos_A = " Mecanico {0} - Rueda {1} retira la llanta vieja"
template_mecanicos_B = " Mecanico {0} - Rueda {1} coloca la llanta nueva"

template_tiempos = " Mecanico {0} gasto: {1}"

# Tiempos de trabajo rueda 1
tiempo_mecanico1_rueda1 = random.randint(0,10)/10
tiempo_mecanico2_rueda1 = random.randint(0,10)/10

# Tiempos de trabajo rueda 2
tiempo_mecanico1_rueda2 = random.randint(0,10)/10
tiempo_mecanico2_rueda2 = random.randint(0,10)/10

# Tiempos de trabajo rueda 3
tiempo_mecanico1_rueda3 = random.randint(0,10)/10
tiempo_mecanico2_rueda3 = random.randint(0,10)/10

# Tiempos de trabajo rueda 4
tiempo_mecanico1_rueda4 = random.randint(0,10)/10
tiempo_mecanico2_rueda4 = random.randint(0,10)/10

# Conversiones


# Pasos
titulo  =  "Pits en la fórmula 1:"
p1 = "1. Carro llega a boxes"
p2 = "2. Se detiene en el box"
p3 = "3. El vehículo tiene 4 llantas"

# Respuesta
print(titulo)
print("")
print(p1)
print(p2)
print(p3)
print("4. " + template_mecanicos_A.format(1,1))
print("5. " + template_mecanicos_B.format(2,1))


print("6. " + template_mecanicos_A.format(1,2))
print("7. " + template_mecanicos_B.format(2,2))

print("8. " + template_mecanicos_A.format(1,3))
print("9. " + template_mecanicos_B.format(2,3))

print("10. " + template_mecanicos_A.format(1,4))
print("11. " + template_mecanicos_B.format(2,4))

print("")

print("Los tiempos gastados en cada llanta fueron: ")
print("")
print(template_tiempos.format(1, tiempo_mecanico1_rueda1))
print(template_tiempos.format(2, tiempo_mecanico1_rueda1))

print("")
print(template_tiempos.format(1, tiempo_mecanico1_rueda2))
print(template_tiempos.format(2, tiempo_mecanico1_rueda2))

print("")
print(template_tiempos.format(1, tiempo_mecanico1_rueda3))
print(template_tiempos.format(2, tiempo_mecanico1_rueda3))

print("")
print(template_tiempos.format(1, tiempo_mecanico1_rueda4))
print(template_tiempos.format(2, tiempo_mecanico1_rueda4))


