"""
File: filename.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import *


class Staff:

    next_id = 1

    def __init__(self, name: str, age: int):
        self.staff_id = Staff.next_id
        self.__name = name
        self.__age = age
        Staff.next_id += 1

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    name = property(get_name)
    age = property(get_age)

    def __str__(self):
        return f"staff member {self.name} is {self.age} years old"

class ZooKeeper(Staff):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__animals = {}
        self.__enclosures = {}

    # Getter & Setters

    def get_enclosures(self):
        return self.__enclosures

    def set_enclosure(self, enclosure):
        self.__enclosures = enclosure

    def get_animals(self):
        return self.__animals

    #def set_animal(self, animal):
     #   self.__animals[animal.name] = animal

    # Properties

    enclosure = property(get_enclosures, set_enclosure)
    animal = property(get_animals)

    def add_animal (self, new_animal):

        if isinstance(new_animal, Animal) and new_animal not in self.animal:
            self.__animals[new_animal.id] = new_animal
            print(f"{new_animal.name} is now under zookeeper {self.name}'s care")
        else:
            print(f"Unable to add animal {new_animal.name} to the keeper's list")

class Veterinarian(Staff):
   def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__animals = {}
        self.__enclosures = {}







