"""
File: filename.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod
import datetime
from staff import *

class Animal(ABC):

    next_id = 1

    def __init__(self, name: str, age: int, gender: str, diet: str, injured = False, sick = False):
        self.__animal_id = Animal.next_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__diet = diet
        self.__injured = injured
        self.__sick = sick
        self.__enclosure = None

        Animal.next_id += 1

    # Getters

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

    # Properties

    name = property(get_name)
    age = property(get_age)
    gender = property(get_gender)
    injured = property(get_injured)
    sick = property(get_sick)
    enclosure = property(get_enclosure, set_enclosure)

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
        print("Sleep! Sleep!")

class Parrot(Bird):
    def __init__(self, name, age, gender, species, diet, injured, sick, flightless: bool):
        super().__init__(name, age, gender, diet, injured, sick, flightless)
        self.__species = species

    def __str__(self):
        return f"A parrot called {self.__name}"

    def cry(self):
        print("Squark! Squark! Screech!")

    def eat(self):
        print("Eat! Eat!")

    def sleep(self):
        print("Sleep! Sleep!")

class Crocodile(Reptile):
    def __init__(self, name, age, gender, species, diet, injured, sick):
        super().__init__(name, age, gender, diet, injured, sick)
        self.__species = species

    def __str__(self):
        return f"A cunning crocodile called {self.__name}"

    def cry(self):
        print("*cold reptilian stare*")

    def eat(self):
        print("Eat! Eat!")

    def sleep(self):
        print("Sleep! Sleep!")

class Frog(Amphibian):
    def __init__(self, name, age, gender, species, diet, injured, sick):
        super().__init__(name, age, gender, diet, injured, sick)
        self.__species = species

    def __str__(self):
        return f"A frog called {self.__name}"

    def cry(self):
        print("Croak... Croak... Croak...")

    def eat(self):
        print("Eat! Eat!")

    def sleep(self):
        print("Sleep! Sleep!")

class Lionfish(Fish):
    def __init__(self, name, age, gender, species, diet, injured, sick):
        super().__init__(name, age, gender, diet, injured, sick)
        self.__species = species

    def __str__(self):
        return f"A lionfish called {self.__name}"

    def cry(self):
        print("*Blows bubble*")

    def eat(self):
        print("Eat! Eat!")

    def sleep(self):
        print("Sleep! Sleep!")


"""
--------- HEALTH ENTRIES ---------
The following three classes inherit from the abstract base class of HealthEntry 

- BehaviouralConcern
- Illness
- Injury 

Each child class has its own unique attributes whilst sharing some similar base attrbiutes 

"""
class HealthEntry(ABC):

    next_id = 1
    health_entry_instances = []

    def __init__(self, vet, date: datetime, animal, notes: str):
        self.__entry_id = HealthEntry.next_id
        self.__vet = vet
        self.__notes = notes
        self.__date = date
        self.__animal = animal
        HealthEntry.next_id += 1
        HealthEntry.health_entry_instances.append (self)

    # Concrete Getters and Setters

    def get_entry_id(self):
        return self.__entry_id

    def get_vet(self):
        return self.__vet

    def get_notes(self):
        return self.__notes

    def get_date(self):
        return self.__date

    def get_animal(self):
        return self.__animal

    # Concrete Propeties

    id = property(get_entry_id)
    vet = property(get_vet)
    notes = property(get_notes)
    date = property(get_date)
    animal = property(get_animal)

   # Abstract Methods
    @abstractmethod
    def __str__(self):
        return(f"""
        | HEALTH RECORD ENTRY |
        ID: {self.id}
        VET: {self.vet.name}
        DATE/TIME: {self.date.strftime('%H:%M:%S %d/%m/%Y')} 
        NOTES: {self.notes} 
        """)

class BehaviouralConcern(HealthEntry):
    def __init__(self, vet, date, animal, behaviour, observation, notes):
        super().__init__(vet, date, animal, notes)
        self.__behaviour = behaviour
        self.__observation = observation

    # Getters

    def get_behaviour(self):
        return self.__behaviour

    def get_observation(self):
        return self.__observation

    # Properties

    behaviour = property(get_behaviour)
    observationL = property(get_observation)

    def __str__(self):
        return(f"""
        | HEALTH ENTRY - BEHAVIOURAL CONCERN |
        ID: {self.id}
        VET: {self.vet.name}
        DATE/TIME: {self.date.strftime('%H:%M:%S %d/%m/%Y')} 
        BEHAVIOUR: {self.behaviour}
        OBSERVATION: {self.observation} 
        NOTES: {self.notes} """)

class Injury(HealthEntry):

    def __init__(self, vet, date, animal, injury, treatment, notes):
        super().__init__(vet, date, animal, notes)
        self.__injury = injury
        self.__treatment = treatment

    # Getters

    def get_injury(self):
        return self.__injury

    def get_treatment(self):
        return self.__treatment

    # Properties

    injury = property(get_injury)
    treatment = property(get_treatment)

    def __str__(self):
        return(f"""
        | HEALTH ENTRY - INJURY |
        ID: {self.id}
        VET: {self.vet.name}
        DATE/TIME: {self.date.strftime('%H:%M:%S %d/%m/%Y')} 
        INJURY: {self.injury}
        TREATMENT: {self.treatment}
        NOTES: {self.notes} """)

class Illness(HealthEntry):

    def __init__(self, vet, date, animal, illness, medication, notes):
        super().__init__(vet, date, animal, notes)
        self.__illness = illness
        self.__medication = medication

    # Getters

    def get_illness(self):
        return self.__illness

    def get_medication(self):
        return self.__medication

    # Properties

    illness = property(get_illness)
    medication = property(get_medication)

    def __str__(self):
        return(f"""
        | HEALTH ENTRY - ILLNESS |
        ID: {self.id}
        VET: {self.vet.name}
        DATE/TIME: {self.date.strftime('%H:%M:%S %d/%m/%Y')} 
        ILLNESS: {self.injury}
        MEDICATION: {self.treatment}
        NOTES: {self.notes} """)


"""
--------- HEALTH RECORD ---------
The following class is used to store the multiple health entries for an individual animal

- Unique to an animal
- Stores health entries in a dictionary
- Can be used to report 
"""

class HealthRecord:

    def __init__(self, record_id: int, animal, entries: dict):
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

        """
        Removes a health entry from the health record

        Performs a check to make sure the entry is in the health record

        """

        if entry_key in self.__entries:
            del self.__entries[entry_key]
            print(f"Health entry with ID: {entry_key} removed successfully")
        else:
            print("No such entry exists within this health record")
