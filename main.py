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

bessy = Chimpanzee("Bessy", 20, "Female", "Common Chimpanzee", "fresh fruit", False, False)
becky  = Parrot("Becky", 9, "Female", "Sulphur Crested Cockatoo", "pine nuts", False, False, False)
allan = Crocodile("Allan", 50, "Male", "Saltwater Crocodile", "chicken", False, False)
fergus = Frog("Fergus", 12, "Male", "Green Tree Frog", "meal worms", False, False)
marlin = Lionfish("Marlin", 3, "Male", "Red Lionfish", "krill", False, False)


enclosure = Enclosure("Sunset", 300, "Tropical",[Bird, Mammal, Reptile])
enclosure_2 = Enclosure("Borealis", 500,"Arctic",[Mammal])
enclosure_3 = Enclosure("Atlantis", 1000,"Underwater", [Fish])
enclosure_4 = Enclosure("Endor", 10, "Forest", [Amphibian])
enclosure_5 = Enclosure("Croclave", 300,"Mangrove", [Reptile, Amphibian])

zac = ZooKeeper("Zac", 30)
maddy = ZooKeeper("Maddy", 23)
tom = ZooKeeper("Tom", 53)
sarah = ZooKeeper("Sarah", 41)

reece = Veterinarian("Reece", 42)
monica = Veterinarian("Monica", 60)
jimmy = Veterinarian("Jimmy", 25)

record = HealthRecord(213, allan, {})

entry_1 = Illness(monica, datetime.datetime.now(), allan, "Stomach Ache", "N/A", "observe overnight for change in symptoms")
entry_2 = BehaviouralConcern(jimmy, datetime.datetime.now(), allan, "Aggression", "Attempted to bite keeper", "leave alone for 24hrs")
entry_3 = Injury(reece, datetime.datetime.now(), allan, "Abrasion", "bandage applied", "Brushed up against metal fence and cut leg")

record.add_entry(entry_1)
record.add_entry(entry_2)
record.add_entry(entry_3)

zac.enclosure = enclosure
maddy.enclosure = enclosure_2
maddy.enclosure = enclosure

enclosure.occupants = allan
enclosure.occupants = bessy
enclosure.occupants = marlin
enclosure.remove_occupant(marlin)
enclosure_4.occupants = fergus


print(record)
