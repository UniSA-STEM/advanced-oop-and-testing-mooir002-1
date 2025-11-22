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

    def remove_staff(self, staff):
        from staff import Staff
        if not isinstance(staff, Staff):
            raise TypeError("staff must be of type Staff")
        self.staff.remove(staff)
        print(f'"{staff.name}" is no longer working at {self.name} zoo')

    def remove_animal(self, animal):
        from animal import Animal
        if not isinstance(animal, Animal):
            raise TypeError("staff must be of type Staff")
        self.animals.remove(animal)
        print(f'"{animal.name}" no longer resides at {self.name} zoo')

    def remove_enclosure(self, enclosure):
        from enclosure import Enclosure
        if not isinstance(enclosure, Enclosure):
            raise TypeError("staff must be of type Staff")
        self.enclosures.remove(enclosure)
        print(f'"{enclosure.name}" has been removed from {self.name} zoo')

    def report_staff(self):
        print(f"| STAFF LIST - {self.name} |\n")
        report = ""
        counter = 1
        for x in self.staff:
            report += (f"| STAFF MEMBER {counter} |\n ID: {x.staff_id}\n NAME: {x.name}\n ROLE: {x.__class__.__name__.lower()}\n\n")
            counter += 1
        print(report)

    def report_enclosures(self):
        print(f"| ENCLOSURE LIST - {self.name} |\n")
        report = ""
        counter = 1
        for x in self.enclosures:
            report += (f"| ENCLOSURE {counter} |\nID: {x.enclosure_id}\nNAME: {x.name}\nNUMBER OF OCCUPANTS: {len(x.occupant)}\n\n")
            counter += 1
        print(report)
        print("----------------")

    def report_animals(self):
        print(f"| ANIMAL LIST - {self.name} |\n")
        report = ""

        counter = 1
        for x in self.animals:
            report += (
                f"| ANIMAL {counter} |\nID: {x.animal_id()}\nNAME: {x.name}\nENCLOSURE: {x.enclosure.name}\nSICK: {x.sick}\nINJURED: {x.injured}\n\n")
            counter += 1
        print(report)
        print("----------------")

    def report_species(self):
        print(f"| SPECIES LIST - {self.name} |")
        list = []
        report = ""
        for animal in self.animals:
            #species = animal.__class__.__name__.lower()
            species = animal.species
            if species in list:
                pass
            else:
                list.append(species)
                report += f"- {species}\n"
        print(f'Number of unique species: {len(list)}')
        print(report)

    def report_categories(self):
        print(f"| ANIMAL CATEGORY LIST - {self.name} |")
        list = []
        report = ""
        for animal in self.animals:
            category = animal.__class__.__name__.lower()
            if category in list:
                pass
            else:
                list.append(category)
                report += f"- {category}\n"
        print(f'Unique animal categories: {len(list)}')
        print(report)