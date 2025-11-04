"""
File: filename.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""



class Animal:
    def __init__(self, name: str, age: int, gender: str, species: str, diet: str):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__species = species
        self.__diet = diet

    # Getters and setters

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

    # Methods

    def cry(self):
        print(f"{self.__name} is crying out")

    def eat(self):
        print(f"{self.__name} is having a feed... *om nom nom*")

    def sleep(self):
        print(f"{self.__name} is now asleep... Zzzzz...")


    # Properties
    classification = property(get_species, set_species)
    name = property(get_name)
    age = property(get_age)
    gender = property(get_gender)
    diet = property(get_diet)

class Bird(Animal):
    def __init__(self, name, age, gender, species, diet, flightless: bool):
        super().__init__(name, age, gender, species, diet)
        self.__flightless = flightless

    def __str__(self):
        if self.__flightless:
            return f"A flightless feathered friend called {self.name}"
        else:
            return f"A feathered friend called {self.name}"

    def cry(self):
        print ("Squark! Chirp! Whistle!")

    #def fly(self):