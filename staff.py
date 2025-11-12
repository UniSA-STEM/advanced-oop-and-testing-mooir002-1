"""
File: filename.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import *
from enclosure import Enclosure


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

    def __str__(self):
        return f"A zoo keeper called {self.name}"

    # Getter & Setters

    def get_enclosures(self):
        return self.__enclosures

    def set_enclosure(self, new_enclosure):
        if isinstance(new_enclosure, Enclosure) and new_enclosure not in self.__enclosures.values():
            self.__enclosures[new_enclosure] = new_enclosure
            print(f"{self.name} is now responsible for the {new_enclosure.name} enclosure")
        else:
            print(f"Unable to add the {new_enclosure.name} enclosure to the keeper's list")

    def get_animals(self):
        return self.__animals

    def set_animal(self, new_animal):
        if isinstance(new_animal, Animal) and new_animal not in self.animal.values():
            self.__animals[new_animal.id] = new_animal
            print(f"{new_animal.name} is now under zookeeper {self.name}'s care")
        else:
            print(f"Unable to add animal {new_animal.name} to the keeper's list")

    # Properties

    enclosure = property(get_enclosures, set_enclosure)
    animal = property(get_animals, set_animal)

    #TODO - complete the feeding method
    #def feed_animal(self, animal):

class Veterinarian(Staff):
   def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__animals = {}
        self.__enclosures = {}

   def __str__(self):
        return f"A veterinarian called {self.name}"

   #TODO - complete the health check method
   #def health_check(self, animal):








