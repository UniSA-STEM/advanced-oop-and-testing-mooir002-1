"""
File: filename.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""



class Animal:
    def __init__(self, name, age, species, category):
        self.name = name
        self.age = age
        self.species = species
        self.category = category

    def cry(self):
        print("woof!")

    def eat(self):
        print("munch, munch, munch")

    def sleep(self):
        print("Zzzzz")

class Mammal(Animal):
    def __init__(self, name, age, species, category):
        super().__init__(name, age, species, category)

class Reptile(Animal):
    def __init__(self, name, age, species, category):
        super().__init__(name, age, species, category)

class Bird(Animal):
    def __init__(self, name, age, species, category):
        super().__init__(name, age, species, category)

class Parrot(Bird):
    def __init__(self, name, age, species, category):
        super().__init__(name, age, species, category)

bob = Parrot("bob", age=5, species="parrot", category="Bird")

bob.eat()
bob.sleep()