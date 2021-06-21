# Declaración de variable global
undefined = 'unknown!!!'
person_description_template = "My name is {0}. I'm a {1} years old {3}. I'm {2} urinated."


class Animal:

    sex = undefined

    def __init__(self, sex):
        self.sex = sex
    
    def sleep(self):
        print("zzzzzZZZZZZZZZzzzzzZZZZzzz")

    def eat(self):
        print("I'm eating.... Yummy!")

# Creación clase persona
class Person(Animal):
    
    # Declaración de atributos
    name = undefined
    lastname = undefined
    age = undefined
    is_urinated = False

    #Declarar el constructor
    def __init__(self, name, lastname, age):
        super().__init__("N/A")
        self.name = name
        self.lastname = name
        self.age = age

    def describe_yourself(self):
        if not self.is_urinated:
            print(person_description_template.format(self.name, self.age, "not", self.sex))
        else:
            print(person_description_template.format(self.name, self.age, "", self.sex))
        

# Creación de la clase Dog
class Dog(Animal):
    # Declaración de atributos
    name = undefined
    race = undefined
    age = undefined
    owner = undefined

    def __init__(self):
        super().__init__("N/A")

    # Definición de funcion (métodos)
    def bark(self):
        print("Woof! WOOOOF!")

    def describe_yourself(self):
        self.bark()
        print("My name is ", self.name, "I'm a ", self.age, "years old dog")
        self.bark
    
    def to_pee(self, person):
        person.is_urinated = True
        print("The dog has urinated", person.name)

    def to_pee_owner(self):
        self.to_pee(self.owner)

    def eat(self):
        super().eat()
        self.bark()


# Creación de los objetos

persona1 = Person("Diana", "Villanueva", 25) # Creación de la persona1

person2 = Person("Luis", "Olarte", 25) # Creación de la persona1

dog_Diana = Dog() # Creación de la mascota de Diana
dog_Diana.name = "Andy"
dog_Diana.age = 2
dog_Diana.owner = persona1


persona1.eat()
dog_Diana.eat()


