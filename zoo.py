"""
File: zoo.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Zoo:

    def __init__(self, name:str):

        if not isinstance(name, str):
            raise TypeError("name must be a string")

        self.__name = name
        self.__staff = []
        self.__animals = []
        self.__enclosures = []

    def get_name(self):
        return self.__name

    def get_staff(self):
        return self.__staff

    def get_animals(self):
        return self.__animals

    def get_enclosures(self):
        return self.__enclosures

   # properties

    name = property(get_name)
    staff = property(get_staff)
    animals = property(get_animals)
    enclosures = property(get_enclosures)

    # methods

    def add_staff(self, staff):
        from staff import Staff
        if not isinstance(staff, Staff):
            raise TypeError("staff must be of type Staff")
        self.staff.append(staff)
        print(f'"{staff.name}" now works at {self.name} zoo')

    def add_animal(self, animal):
        from animal import Animal
        if not isinstance(animal, Animal):
            raise TypeError("animal must be of type Animal")
        self.animals.append(animal)
        print(f'"{animal.name}" now resides at {self.name} zoo')

    def add_enclosure(self, enclosure):
        from enclosure import Enclosure
        if not isinstance(enclosure, Enclosure):
            raise TypeError("enclosure must be of type Enclosure")
        self.enclosures.append(enclosure)
        print(f'"{enclosure.name}" enclosure has been added to {self.name} zoo')

    def report_staff(self):
        print(f"| STAFF LIST - {self.name} |\n")
        report = ""
        counter = 1
        for x in self.__staff:
            report += (f"| STAFF MEMBER {counter} |\n ID: {x.staff_id}\n NAME: {x.name}\n ROLE: {x.__class__.__name__.lower()}\n\n")
            counter += 1
        print(report)

    def report_enclosures(self):
        print(f"| ENCLOSURE LIST - {self.name} |\n")
        report = ""
        counter = 1
        for x in self.__enclosures:
            report += (f"| ENCLOSURE {counter} |\n ID: {x.enclosure_id}\n NAME: {x.name}\n {len(x.occupants)}\n")

    # TODO - Add a method to list all the animals by species