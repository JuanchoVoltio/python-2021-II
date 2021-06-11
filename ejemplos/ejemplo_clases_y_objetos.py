undefined = 'unknown'

class Dog:
    #Atributes (state)
    name = undefined
    race = undefined
    age = undefined
    sex = undefined


    #Functions (methods, behaviors)
    def bark(self):
        print("Wooof! WOOOOF!")

    def sleep(self):
        print("zzzZzZZzZZZ")

    def describe_yourself(self, command):
        self.bark()
        print("My name is ", self.name, "I'm a ", self.age, "years old dog")
        self.bark()
        print("I'm ", command, "ing")
        self.bark()


dog_diana = Dog() #011
dog_luis = Dog() #012
dog_diana.name = "Andy"
dog_luis.name = "Ginger"
dog_diana.age = 2
dog_luis.age = 5
dog_diana.describe_yourself("Roll")
dog_luis.describe_yourself("jump")
