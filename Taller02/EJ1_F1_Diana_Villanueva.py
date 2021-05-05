import random


titulo = "Pits en la fórmula 1:"
# Mecanicos rueda 1
mecanico1_rueda1 = "Mecanico 1 - Rueda 1"
mecanico2_rueda1 = "Mecanico 2 - Rueda 1"

# Mecanicos rueda 2
mecanico1_rueda2 = "Mecanico 1 - Rueda 2"
mecanico2_rueda2 = "Mecanico 2 - Rueda 2"

# Mecanicos rueda 3
mecanico1_rueda3 = "Mecanico 1 - Rueda 3"
mecanico2_rueda3 = "Mecanico 2 - Rueda 3"

# Mecanicos rueda 4
mecanico1_rueda4 = "Mecanico 1 - Rueda 4"
mecanico2_rueda4 = "Mecanico 2 - Rueda 4"

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

# Respuesta
titulo  =  "Pits en la fórmula 1:"
p1 = "1. Carro llega a boxes"
p2 = "2. Se detiene en el box"
p3 = "3. El vehículo tiene 4 llantas"
p4 = "4. " + mecanico1_rueda1 + " retira la llanta vieja "
p5 = "5. " + mecanico2_rueda1 + " coloca la llanta nueva "

p6 = "6. " + mecanico1_rueda2 + " retira la llanta vieja " 
p7 = "7. " + mecanico2_rueda2 + " coloca la llanta nueva "

p8 = "8. " + mecanico1_rueda3 + " retira la llanta vieja " 
p9 = "9. " + mecanico2_rueda3 + " coloca la llanta nueva " 

p10 = "10. " + mecanico1_rueda4 + " retira la llanta vieja " 
p11 = "11. " + mecanico2_rueda4 + " coloca la llanta nueva " 

p12 = "12. Al terminar el cambio de las llantas el vehiculo sale de pits y se reincorpora a la pista."


# Conversiones
t_m1_r1 = str(tiempo_mecanico1_rueda1)
t_m2_r1 = str(tiempo_mecanico2_rueda1)

t_m1_r2 = str(tiempo_mecanico1_rueda2)
t_m2_r2 = str(tiempo_mecanico2_rueda2)

t_m1_r3 = str(tiempo_mecanico1_rueda3)
t_m2_r3 = str(tiempo_mecanico2_rueda3)

t_m1_r4 = str(tiempo_mecanico1_rueda4)
t_m2_r4 = str(tiempo_mecanico2_rueda4)

print(titulo)
print("")
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)
print(p11)
print(p12)
print("")

print("Los tiempos gastados en cada llanta fueron: ")
print("")
print(mecanico1_rueda1 + " gasto: " + t_m1_r1)
print(mecanico2_rueda1 + " gasto: " + t_m2_r1)

print("")
print(mecanico1_rueda2 + " gasto: " + t_m1_r2)
print(mecanico2_rueda2 + " gasto: " + t_m2_r2)

print("")
print(mecanico1_rueda3 + " gasto: " + t_m1_r3)
print(mecanico2_rueda3 + " gasto: " + t_m2_r3)

print("")
print(mecanico1_rueda4 + " gasto: " + t_m1_r4)
print(mecanico2_rueda4 + " gasto: " + t_m2_r4)
