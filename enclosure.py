"""
File: filename.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod

enclosure_list = []

class Enclosure:

    next_id = 1

    def __init__(self, name: str, size: int, biome: str, animals: list):
        self.__enclosure_id = Enclosure.next_id
        self.__name = name
        self.__size = size
        self.__biome = biome
        self.__cleanliness = float(100)
        self.__occupants = []
        self.__animals = animals
        Enclosure.next_id += 1
        enclosure_list.append(self)

    # Getters & Setters

    def get_enclosure_id(self):
        return self.__enclosure_id

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_biome(self):
        return self.__biome

    def get_cleanliness(self):
        return self.__cleanliness

    def set_cleanliness(self, value):
        self.__cleanliness = value

    def get_occupants(self):
        return self.__occupants

    def set_occupant(self, new_occupant):

        for permitted_type in self.animals:

            if isinstance(new_occupant, permitted_type):
                self.__occupants.append(new_occupant)
                print (f"added a new occupant '{new_occupant.name}' to the {self.name} enclosure")
                new_occupant.enclosure = self
                break
        else:
            print(f"The {self.name} enclosure is not equipped to house {new_occupant.name}")

    def get_animals(self):
        return self.__animals

    def get_animal_names(self):
        output = ""
        for item in self.__animals:
            output += (f"{item.__name__}, ")
        output = output[:-2]
        return output

    # Properties

    enclosure_id = property(get_enclosure_id)
    name = property(get_name)
    size = property(get_size)
    biome = property(get_biome)
    cleanliness = property(get_cleanliness)
    occupant = property(get_occupants, set_occupant)
    animals = property(get_animals)
    animal_names = property(get_animal_names)

    # Methods

    def __str__(self):
        return (f"| ZOO ENCLOSURE |\nNAME: {self.name}\nBIOME: {self.biome}\nSIZE: {self.size}m\u00b2\nCLEANLINESS: {self.cleanliness}\nPERMITTED ANIMALS: {self.animal_names}\nOCCUPANTS: Currently housing {len(self.occupant)} animal(s)")

    def remove_occupant(self, occupant):

        if occupant in self.__occupants:
            self.__occupants.remove(occupant)
            print(f"REMOVED OCCUPANT: '{occupant.name}' from the {self.name} enclosure")
            occupant.enclosure = None
        else:
            print(f"UNABLE TO REMOVE: {occupant.name} is not currently in {self.name}")

    def list_occupants(self):
        output = ""
        for item in self.occupant:
            output += (f"{item.name}, ")
        output = output[:-2]
        return f"current occupants of the {self.name} enclosure: {output}"

    def clean_enclosure(self, keeper: 'ZooKeeper'):
        from staff import ZooKeeper
        if isinstance(keeper, ZooKeeper) and self in keeper.enclosure:
            print("enclosure is now clean!")
        else:
            print(f'{keeper.name} is not able to clean this enclosure')







