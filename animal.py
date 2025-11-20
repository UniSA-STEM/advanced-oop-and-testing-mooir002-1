"""
File: animal.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod
from health_record import HealthRecord

class Animal(ABC):

    next_id = 1

    def __init__(self, name: str, age: int, gender: str, diet: str, injured = False, sick = False):
        self._animal_id = Animal.next_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__diet = diet
        self.__injured = injured
        self.__sick = sick
        self.__enclosure = None
        self.__health_record = HealthRecord(self)

        Animal.next_id += 1

    # Getters

    def get_animal_id(self):
        return self._animal_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_diet(self):
        return self.__diet

    def get_injured(self):
        return self.__injured

    def get_sick(self):
        return self.__sick

    def get_enclosure(self):
        return self.__enclosure

    def set_enclosure(self, enclosure):
        self.__enclosure = enclosure

    def get_health_record(self):
        return self.__health_record

    # Properties
    animal_id = (get_animal_id)
    name = property(get_name)
    age = property(get_age)
    gender = property(get_gender)
    injured = property(get_injured)
    sick = property(get_sick)
    enclosure = property(get_enclosure, set_enclosure)
    health_record = property(get_health_record)

    # Abstract Methods

    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def get_health_record(self):
        return self.__health_record

    # Methods

    #TODO - Add a method to list all the animals by species

"""
--------- CORE CLASSES OF ANIMALS ---------
Using the taxonomical classification system each zoo animal falls under at least one of the following five classes.

1) Mammal
2) Bird
3) Reptile
4) Amphibian
5) Fish

"""

class Mammal(Animal):

    def __init__(self, name, age, gender, diet, injured, sick):
        super().__init__(name, age, gender, diet, injured, sick)

    def __str__(self):
        return f"A mammal called {self.__name}"

    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, gender, diet, injured, sick, flightless: bool):
        super().__init__(name, age, gender, diet, injured, sick)
        self.__flightless = flightless

    def __str__(self):
        if self.__flightless:
            return f"A flightless feathered friend called {self.__name}"
        else:
            return f"A feathered friend called {self.__name}"

    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    #TODO - Add a flying class for birds
    #def fly(self):

class Reptile(Animal):

    def __init__(self, name, age, gender, diet, injured, sick):
        super().__init__(name, age, gender, diet, injured, sick)

    def __str__(self):
        return f"A cold blooded reptile called {self.__name}"

    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Amphibian(Animal):

    def __init__(self, name, age, gender, diet, injured, sick):
        super().__init__(name, age, gender, diet, injured, sick)

    def __str__(self):
        return f"A slippery soul called {self.__name}"

    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Fish(Animal):

    def __init__(self, name, age, gender, diet, injured, sick):
        super().__init__(name, age, gender, diet, injured, sick)

    def __str__(self):
        return f"A wet and wild sea creature called {self.__name}"

    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

"""
--------- ANIMAL SPECIES ---------
The following species all inherit from the five main classes of animals.
I've included the names of both instances for each species (found in main.py) for clarity. 

- Chimpanzee (Mammal) - Bessie
- Parrot (Bird) - Beckie
- Crocodile (Reptile) - Allan
- Frog (Amphibian) - Fergus
- Lionfish (Fish) - Marlin 

"""

class Chimpanzee(Mammal):
    def __init__(self, name, age, gender, species, diet, injured, sick):
        super().__init__(name, age, gender, diet, injured, sick)
        self.__species = species

    def __str__(self):
        return f"A cheeky chimp called {self.__name}"

    def cry(self):
        print("Oooooo! Ooohh! Ahhh! AAAAHHHH!")

    def eat(self):
        print("Eat! Eat!")

    def sleep(self):
        print("Zzzzzzzzzzzz...")

class Parrot(Bird):
    def __init__(self, name, age, gender, species, diet, injured, sick, flightless: bool):
        super().__init__(name, age, gender, diet, injured, sick, flightless)
        self.__species = species

    def __str__(self):
        return f"A parrot called {self.__name}"

    def cry(self):
        print("Squark! Squark! Screech!")

    def eat(self):
        print("peck... peck. peck.")

    def sleep(self):
        print("Zzzzzz...")

class Crocodile(Reptile):
    def __init__(self, name, age, gender, species, diet, injured, sick):
        super().__init__(name, age, gender, diet, injured, sick)
        self.__species = species

    def __str__(self):
        return f"A cunning crocodile called {self.__name}"

    def cry(self):
        print("*cold reptilian stare*")

    def eat(self):
        print("chomp, chomp, chomp")

    def sleep(self):
        print("Zzzzzz...")

class Frog(Amphibian):
    def __init__(self, name, age, gender, species, diet, injured, sick):
        super().__init__(name, age, gender, diet, injured, sick)
        self.__species = species

    def __str__(self):
        return f"A frog called {self.__name}"

    def cry(self):
        print("Croak... Croak... Croak...")

    def eat(self):
        print("... ... ... gulp!")

    def sleep(self):
        print("Zzzzzz....")

class Lionfish(Fish):
    def __init__(self, name, age, gender, species, diet, injured, sick):
        super().__init__(name, age, gender, diet, injured, sick)
        self.__species = species

    def __str__(self):
        return f"A lionfish called {self.__name}"

    def cry(self):
        print("*Blows bubble*")

    def eat(self):
        print("nibble... nibble...")

    def sleep(self):
        print("Zzzzzz....")




