"""
File: filename.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""
from zoo import Zoo


class Staff:

    from zoo import Zoo
    next_id = 1

    def __init__(self, name: str, age: int):
        self._staff_id = Staff.next_id
        self.__name = name
        self.__age = age

        Staff.next_id += 1

    def get_staff_id(self):
        return self._staff_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    staff_id = property(get_staff_id)
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
        from enclosure import Enclosure
        if isinstance(new_enclosure, Enclosure) and new_enclosure not in self.__enclosures.values():
            self.__enclosures[new_enclosure] = new_enclosure
            print(f"{self.name} is now responsible for the {new_enclosure.name} enclosure")
        else:
            print(f"Unable to add the {new_enclosure.name} enclosure to the keeper's list")

    def get_animals(self):
        return self.__animals

    def add_animal(self, new_animal: 'Animal'):
        from animal import Animal
        if isinstance(new_animal, Animal) and new_animal not in self.animal.values():
            self.__animals[new_animal.animal_id] = new_animal
            print(f"{new_animal.name} is now under zookeeper {self.name}'s care")
        else:
            print(f"Unable to add {new_animal.name} to the keeper's list")

    def remove_animal(self, new_animal: 'Animal'):
        from animal import Animal
        if isinstance(new_animal, Animal) and new_animal in self.animal.values():
            del self.__animals[new_animal.animal_id]
            print(f"{new_animal.name} has been removed from zookeeper {self.name}'s care")
        else:
            print(f"Unable to remove {new_animal.name} from the keeper's list")

    # Properties

    enclosure = property(get_enclosures, set_enclosure)
    animal = property(get_animals)

    def feed_animal(self, animal):
        from animal import Animal
        if isinstance(animal, Animal) and animal in self.animal.values():
            print(f"{animal.name} is being fed...")
            animal.eat()

        else:
            print(f"{self.name} is unable to feed {animal.name}")

class Veterinarian(Staff):
   def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__animals = {}
        self.__enclosures = {}

   def __str__(self):
        return f"A veterinarian called {self.name}"

   #TODO - complete the health check method
   #def health_check(self, animal):








