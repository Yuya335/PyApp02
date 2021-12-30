

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printName(self):
        print('My name is ' + self.name + '.')

    def printAge(self):
        print("I'm " + str(self.age) + " years old.")