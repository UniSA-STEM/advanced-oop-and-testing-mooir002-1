"""
File: health_record.py
Description: Where health entries are stored
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""


"""
--------- HEALTH RECORD ---------
The following class is used to store the multiple health entries for an individual animal

- Unique to each animal
- Stores health entries in a dictionary
- Can be used to generate reports
- Is automatically created when an animal is instantiated 

"""

"""
In order to remove circular imports I'm using the TYPE_CHECKING class to prevent 
all the imports from running at startup. They will now only be called at the appropriate time.

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from animal import Animal
    from health_entries import HealthEntry, Illness, Injury, BehaviouralConcern

class HealthRecord:

    record_id = 1

    def __init__(self, animal: "Animal"):
        from animal import Animal
        self._record_id = HealthRecord.record_id
        self.__animal = animal
        self.__entries = {}
        HealthRecord.record_id += 1

        if not isinstance(animal, Animal):
            raise TypeError("animal must be an Animal object")

    # Getters and setters

    def get_id(self):
        return self._record_id

    def get_animal(self):
        return self.__animal

    def get_entries(self):
        return self.__entries

    def set_entry(self, new_entry):
        if self.__entries == {}:
            new_entry_key = 0
        else:
            new_entry_key = len(self.__entries)+1
        self.__entries[new_entry_key] = new_entry

    def get_illness_count(self):
        from health_entries import Illness
        count = 0
        for entry in self.__entries.values():
            if isinstance(entry, Illness):
                count += 1
        return count

    def get_injury_count(self):
        from health_entries import Injury
        count = 0
        for entry in self.__entries.values():
            if isinstance(entry, Injury):
                count += 1
        return count

    def get_behavioural_concern_count(self):
        from health_entries import BehaviouralConcern
        count = 0
        for entry in self.__entries.values():
            if isinstance(entry, BehaviouralConcern):
                count += 1
        return count

    # Properties
    entries = property(get_entries)
    animal = property(get_animal)
    injury_count = property(get_injury_count)
    illness_count = property(get_illness_count)
    behavioural_count = property(get_behavioural_concern_count)

    # Methods

    def __str__(self):

        sick = ""
        if self.animal.sick == True:
            sick = "YES"
        else:
            sick = "NO"

        injured = ""
        if self.animal.injured == True:
            injured = "YES"
        else:
            injured = "NO"

        return f"Health Record | ID: {self._record_id} | Animal: {self.__animal.name} | Total Entries: {len(self.__entries)}\n------------------\nIllness Entries: {self.illness_count}\nInjury Entries: {self.injury_count}\nBehavioural Entries: {self.behavioural_count}\n------------------\nCurrently sick: {sick}\nCurrently injured: {injured}\n\n"

    def add_entry(self, health_entry):
        from health_entries import HealthEntry

        """Checks to see if the health entry is a valid:
                - Does the object exist?
                - Does the health entry animal match the animal in the health record?
           Uses the set_entry function to add the entry to the record:
                - dictionary key is an auto-generated number
                - dictionary value is the entry object
           Type validation is enforced to ensure that only health entries are added"""

        if isinstance(health_entry, HealthEntry) and health_entry.animal == self.__animal:
            self.set_entry(health_entry)
        else:
            print("What you entered is either not a valid health entry, or is a health entry for a different animal")
            raise TypeError("The entry must be of type HealthEntry")

    def remove_entry(self, entry_key):

        """
        Removes a health entry from the health record
        The entry key is separate to the health entry ID
        Performs a check to make sure the entry is in the health record

        """

        if entry_key in self.entries:
            print(f"Health entry with (ID: {self.entries[entry_key].id} and KEY: {entry_key}) was successfully removed from {self.animal.name}'s health record")
            del self.entries[entry_key]
        else:
            print("No such entry exists within this health record")