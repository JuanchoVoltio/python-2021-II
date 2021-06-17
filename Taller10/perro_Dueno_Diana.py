# Declaración de variable global
undefined = 'unknown'

# Creación clase persona
class Person:
    # Declaración de atributos
    name = undefined
    lastname = undefined
    age = undefined
    sex = undefined

# Creación de la clase Dog
class Dog:
    # Declaración de atributos
    name = undefined
    race = undefined
    age = undefined
    sex = undefined

    # Definición de funcion (métodos)
    def bark(self):
        print("Woof! WOOOOF!")

    def sleep(self):
        print("zzzzzZZZZZZZZZzzzzzZZZZzzz")

    def describe_yourself(self):
        self.bark()
        print("My name is ", self.name, "I'm a ", self.age, "years old dog")
        self.bark

    def eat(self):
        print("The dog eats his croquettes")

    def to_pee(self):
        print("The dog has urinated on its owner")


# Creación de los objetos

persona1 = Person() # Creación de la persona1
persona1.name = "Diana"
persona1.lastname = "Villanueva"
persona1.age = 25
persona1.sex = "Female"


dog_Diana = Dog() # Creación de la mascota de Diana
dog_Diana.name = "Andy"
dog_Diana.age = 2
dog_Diana.describe_yourself()
