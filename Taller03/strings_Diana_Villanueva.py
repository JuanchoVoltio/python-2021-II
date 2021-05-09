# replace(): Método que reemplaza una frase específica por otra frase específica
print("REPLACE:" )
txt = "I like bananas"
x = txt.replace("bananas","apples")
print(x)
print("")

# split(): Método que divide una cadena en una lista.
print("SPLIT:" )
cadena = "Welcome to the jungle"
lista = cadena.split()
print(lista)
print("")

# strip(): Remueve espacios o el caracter entregado como argumento de la función.
print("STRIP:" )
texto = ",,,,,rrttgg.....banana.....rrr"
nuevo_texto = texto.strip(",.grt")
print(nuevo_texto)
print("")

# isalpha(): Método que devuelve True si todos los caracteres son letras del alfabeto (a-z).
print("ISALPHA:" )
mi_texto = "CompanyX"
resultado = mi_texto.isalpha()
print(resultado)
print("")

# istitle(): Método que devuelve True si todas las palabras de un texto comienzan con mayúsculas.
print("ISTITLE: ")
cadena2 = "Hello, And Welcome To My World!"
res = cadena2.istitle()
print(res)
print("")

# isupper(): Método que devuelve True si todos los caracteres están en mayúsculas.
print("ISUPPER: ")
mayusculas = "THIS IS NOW!"
respuesta = mayusculas.upper()
print(respuesta)
