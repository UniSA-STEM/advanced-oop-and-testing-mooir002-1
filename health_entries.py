"""
File: health_entries.py
Description: Where health entries are stored
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""


from abc import ABC, abstractmethod

"""
In order to remove circular imports I'm using the TYPE_CHECKING class to prevent 
all the imports from running at startup. They will now only be called at the appropriate time.

"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from animal import Animal

"""
--------- HEALTH ENTRIES ---------

The following three classes inherit from the abstract base class of HealthEntry 

- BehaviouralConcern
- Illness
- Injury 

Each child class has its own unique attributes whilst sharing some similar base attributes.

"""

class HealthEntry(ABC):

    import datetime
    next_id = 1
    health_entry_instances = []

    def __init__(self, vet, date: datetime, animal: "Animal", notes: str):
        from animal import Animal
        self.__entry_id = HealthEntry.next_id
        self.__vet = vet
        self.__notes = notes
        self.__date = date
        self.__animal = animal
        HealthEntry.next_id += 1
        HealthEntry.health_entry_instances.append (self)

        # automatically adds the entry to the animal's health record
        self.__animal.health_record.add_entry(self)

        if not isinstance(animal, Animal):
            raise TypeError("animal must be an Animal object")

        if not isinstance(notes, str):
            raise TypeError("notes must be a string")

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
        pass

class BehaviouralConcern(HealthEntry):
    def __init__(self, vet, date, animal, behaviour, observation, notes):
        super().__init__(vet, date, animal, notes)
        self.__behaviour = behaviour
        self.__observation = observation

        if not isinstance(behaviour, str):
            raise TypeError("behaviour must be a string")

        if not isinstance(observation, str):
            raise TypeError("observation must be a string")

    # Getters

    def get_behaviour(self):
        return self.__behaviour

    def get_observation(self):
        return self.__observation

    # Properties

    behaviour = property(get_behaviour)
    observation = property(get_observation)

    def __str__(self):
        return(f"| HEALTH ENTRY - BEHAVIOURAL CONCERN |\nID: {self.id}\nANIMAL: {self.animal.name}\nVET: {self.vet.name}\nDATE/TIME: {self.date.strftime('%H:%M:%S %d/%m/%Y')}\nBEHAVIOUR: {self.behaviour}\nOBSERVATION: {self.observation}\nNOTES: {self.notes}\n")

class Injury(HealthEntry):

    def __init__(self, vet, date, animal, injury, treatment, notes):
        super().__init__(vet, date, animal, notes)
        self.__injury = injury
        self.__treatment = treatment

        if not isinstance(injury, str):
            raise TypeError("injury must be a string")

        if not isinstance(treatment, str):
            raise TypeError("treatment must be a string")

    # Getters

    def get_injury(self):
        return self.__injury

    def get_treatment(self):
        return self.__treatment

    # Properties

    injury = property(get_injury)
    treatment = property(get_treatment)

    def __str__(self):
        return(f"| HEALTH ENTRY - INJURY |\nID: {self.id}\nANIMAL: {self.animal.name}\nVET: {self.vet.name}\nDATE/TIME: {self.date.strftime('%H:%M:%S %d/%m/%Y')}\nINJURY: {self.injury}\nTREATMENT: {self.treatment}\nNOTES: {self.notes}\n")

class Illness(HealthEntry):

    def __init__(self, vet, date, animal, illness, medication, notes):
        super().__init__(vet, date, animal, notes)
        self.__illness = illness
        self.__medication = medication

        if not isinstance(illness, str):
            raise TypeError("illness must be a string")

        if not isinstance(medication, str):
            raise TypeError("medication must be a string")

    # Getters

    def get_illness(self):
        return self.__illness

    def get_medication(self):
        return self.__medication

    # Properties

    illness = property(get_illness)
    medication = property(get_medication)

    def __str__(self):
        return(f"| HEALTH ENTRY - ILLNESS |\nID: {self.id}\nANIMAL: {self.animal.name}\nVET: {self.vet.name}\nDATE/TIME: {self.date.strftime('%H:%M:%S %d/%m/%Y')}\nILLNESS: {self.illness}\nMEDICATION: {self.medication}\nNOTES: {self.notes}\n")
