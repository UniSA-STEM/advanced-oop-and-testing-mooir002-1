"""
File: filename.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""

import datetime

class Animal:

    next_id = 1

    def __init__(self, name: str, age: int, gender: str, species: str, diet: str, injured = False, sick = False):
        self.__animal_id = Animal.next_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__species = species
        self.__diet = diet
        self.__injured = injured
        self.__sick = sick
        self.__enclosure = None

        Animal.next_id += 1

    # Getters and setters

    def get_id(self):
        return self.__animal_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_species(self):
        return self.__species

    def set_species(self, new_species: str):
        self.__species = new_species

    def get_diet(self):
        return self.__diet

    def get_injured(self):
        return self.__injured

    def set_injured(self, value: bool):
        self.__injured = value

    def get_sick(self):
        return self.__sick

    def set_sick(self):
        return self.__sick

    def get_enclosure(self):
        return self.__enclosure

    def set_enclosure(self, value):
        self.__enclosure = value

    # Methods

    def cry(self):
        print(f"{self.__name} is crying out")

    def eat(self):
        print(f"{self.__name} is having a feed... *om nom nom*")

    def sleep(self):
        print(f"{self.__name} is now asleep... Zzzzz...")


    # Properties
    id = property(get_id)
    classification = property(get_species, set_species)
    name = property(get_name)
    age = property(get_age)
    gender = property(get_gender)
    diet = property(get_diet)
    injured = property(get_injured, set_injured)
    sick = property (get_sick, set_sick)
    enclosure = property(get_enclosure, set_enclosure)

class Bird(Animal):
    def __init__(self, name, age, gender, species, diet, injured, sick, flightless: bool):
        super().__init__(name, age, gender, species, diet, injured, sick)
        self.__flightless = flightless

    def __str__(self):
        if self.__flightless:
            return f"A flightless feathered friend called {self.name}"
        else:
            return f"A feathered friend called {self.name}"

    def cry(self):
        print ("Squark! Chirp! Whistle!")

    #def fly(self):

class Mammal(Animal):

    def __init__(self, name, age, gender, species, diet, injured, sick):
        super().__init__(name, age, gender, species, diet, injured, sick)

    def __str__(self):
        return f"A mammal called {self.name}"

    def cry(self):
        print("*generic mammalian wail*")

class Reptile(Animal):

    def __init__(self, name, age, gender, species, diet, injured, sick):
        super().__init__(name, age, gender, species, diet, injured, sick)

    def __str__(self):
        return f"A cold blooded reptile called {self.name}"

    def cry(self):
        print("*stares coldly*")

class Amphibian(Animal):

    def __init__(self, name, age, gender, species, diet, injured, sick):
        super().__init__(name, age, gender, species, diet, injured, sick)

    def __str__(self):
        return f"A slippery soul called {self.name}"

    def cry(self):
        print("*amphibious sounds*")

class Fish(Animal):

    def __init__(self, name, age, gender, species, diet, injured, sick):
        super().__init__(name, age, gender, species, diet, injured, sick)

    def __str__(self):
        return f"A wet and wild sea creature called {self.name}"

    def cry(self):
        print("*splish, splash, splosh*")


class Parrot(Bird):
    def __init__(self, name, age, gender, species, diet, injured, sick, flightless: bool):
        super().__init__(name, age, gender, species, diet, injured, sick, flightless)

    def __str__(self):
        return f"A parrot called {self.name}"

    def cry(self):
        print("Squark! Squark! Screech!")

class HealthEntry:

    next_id = 1
    health_entry_instances = []

    def __init__(self, observation: str, medication: str, date: datetime, animal: Animal):
        self.__entry_id = HealthEntry.next_id
        self.__observation = observation
        self.__medication = medication
        self.__date = date
        self.__animal = animal
        HealthEntry.next_id += 1
        HealthEntry.health_entry_instances.append (self)

    # Getters and setters

    def get_id(self):
        return self.__entry_id

    def get_observation(self):
        return self.__observation

    def get_medication(self):
        return self.__medication

    def get_date(self):
        return self.__date

    def get_animal(self):
        return self.__animal

    # Properties

    id = property(get_id)
    observation = property(get_observation)
    medication = property(get_medication)
    date = property(get_date)
    animal = property(get_animal)

    # Methods

    def __str__(self):
        return(f"""
        | HEALTH RECORD ENTRY |
        ID: {self.id}
        DATE/TIME: {self.date.strftime('%H:%M:%S %d/%m/%Y')} 
        OBSERVATION: {self.observation} 
        MEDICATION: {self.medication}""")


class HealthRecord:

    def __init__(self, record_id: int, animal: Animal, entries: dict):
        self.__record_id = record_id
        self.__animal = animal
        self.__entries = entries

    # Getters and setters

    def get_id(self):
        return self.__record_id

    def get_animal(self):
        return self.__animal

    def get_entries(self):
        return self.__entries

    def set_entry(self, new_entry_key, new_entry):
        self.__entries[new_entry_key] = new_entry

    # Properties

    entries = property(get_entries)
    animal = property(get_animal)

    # Methods

    def __str__(self):
        return f"Health Record | ID: {self.__record_id} | Animal: {self.__animal.name} | Entries: {len(self.__entries)} "

    def add_entry(self, health_entry):

        """Checks to see if the health entry is a valid:
                - Does the object exist?
                - Does the health entry animal match the animal in the health record?
           Uses the set_entry function to add the entry to the record:
                - dictionary key is the date
                - dictionary value is the entry object
           Type validation is enforced to ensure that only health entries are added"""

        if isinstance(health_entry, HealthEntry) and health_entry.animal == self.__animal:
            self.set_entry(health_entry.id, health_entry)
        else:
            print("What you entered is either not a valid health entry, or is a health entry for a different animal")
            raise TypeError("The entry must be of type HealthEntry")

    def remove_entry(self, entry_key):

        """Removes a health entry from the health record"""

        if entry_key in self.__entries:
            del self.__entries[entry_key]
            print(f"Health entry with ID: {entry_key} removed successfully")
        else:
            print("No such entry exists within this health record")
