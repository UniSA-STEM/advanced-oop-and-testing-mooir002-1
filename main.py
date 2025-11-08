"""
File: filename.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import *
from enclosure import *
from staff import *

tiko = Bird("Tiko", 5, "Male", "Toco Toucan", "fruit", False, False, False)
massa = Bird("Massa", 1, "Female", "Budgee", "seeds", False, False, False)
rex = Mammal("Rex", 10,"Male", "Dog", "meat", False, False)
tommy = Reptile("Tommy", 50, "Male", "Crocodile", "meat", False, False)
martin = Parrot("Martin", 15, "Male", "Parrot", "fruit", False, False, False)

record = HealthRecord(213, tiko, {})
entry = HealthEntry("Tiko is looking good", "N/A", datetime.datetime.now(), tiko)
entry2 = HealthEntry("Tiko is feeling unwell", "Panadol", datetime.datetime.now(), tiko)
entry3 = HealthEntry("Tiko is much improved", "N/A", datetime.datetime.now(), tiko)

enclosure = Enclosure("Sunset", 300, "Tropical",[Bird, Mammal])
enclosure_2 = Enclosure("Borealis", 500,"Arctic",[Mammal])
enclosure_3 = Enclosure("Atlantis", 1000,"Underwater", [Fish])
enclosure_4 = Enclosure("Endor", 100, "Forest", [Amphibian])

zac = ZooKeeper("Zac", 30)
maddy = ZooKeeper("Maddy", 23)
tom = ZooKeeper("Tom", 53)
sarah = ZooKeeper("Sarah", 41)

reece = Veterinarian("Reece", 42)
monica = Veterinarian("Monica", 60)
jimmy = Veterinarian("Jimmy", 25)

record.add_entry(entry)
record.add_entry(entry2)
record.add_entry(entry3)

zac.enclosure = enclosure
maddy.enclosure = enclosure_2
maddy.enclosure = enclosure

enclosure.occupants = rex
enclosure.occupants = tommy
enclosure.occupants = martin
enclosure.remove_occupant(martin)

print(enclosure)