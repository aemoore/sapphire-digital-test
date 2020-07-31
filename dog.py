class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound):
        print "do you hear that? \'" + sound + "\' " + self.name + " the dog said"