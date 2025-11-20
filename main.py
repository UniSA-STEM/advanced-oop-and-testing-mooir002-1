"""
File: filename.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports all modules into main

from animal import *
from enclosure import *
from staff import *
from zoo import *
import datetime

"""

                --- CREATION OF INSTANCES ---

The following code instantiates all the instances of the classes
we will be using to demonstrate the functionality for this project.

"""

# Creates a new instance of a zoo

adelaide_zoo = Zoo("Adelaide")

# Creates five instances of different kinds of animals

bessy = Chimpanzee("Bessy", 20, "Female", "Common Chimpanzee", "fresh fruit", False, False)
becky  = Parrot("Becky", 9, "Female", "Sulphur Crested Cockatoo", "pine nuts", False, False, False)
allan = Crocodile("Allan", 50, "Male", "Saltwater Crocodile", "chicken", False, False)
fergus = Frog("Fergus", 12, "Male", "Green Tree Frog", "meal worms", False, False)
marlin = Lionfish("Marlin", 3, "Male", "Red Lionfish", "krill", False, False)

# Creates five instances of zoo enclosures

enclosure = Enclosure("Sunset", 300, "Tropical",[Bird, Mammal, Reptile])
enclosure_2 = Enclosure("Borealis", 500,"Arctic",[Mammal])
enclosure_3 = Enclosure("Atlantis", 1000,"Underwater", [Fish])
enclosure_4 = Enclosure("Endor", 10, "Forest", [Amphibian])
enclosure_5 = Enclosure("Croclave", 300,"Mangrove", [Reptile, Amphibian])

# Creates four instances of zookeepers

zac = ZooKeeper("Zac", 30)
maddy = ZooKeeper("Maddy", 23)
tom = ZooKeeper("Tom", 53)
sarah = ZooKeeper("Sarah", 41)

# Creates three instances of vets

reece = Veterinarian("Reece", 42)
monica = Veterinarian("Monica", 60)
jimmy = Veterinarian("Jimmy", 25)

# Creates 20 instances of health entries (x4 for each animal)

entry_1 = Illness(monica, datetime.datetime.now(), allan, "Stomach Ache", "N/A", "observe overnight for change in symptoms")
entry_2 = BehaviouralConcern(jimmy, datetime.datetime.now(), allan, "Aggression", "Attempted to bite keeper", "leave alone for 24hrs")
entry_3 = Injury(reece, datetime.datetime.now(), allan, "Abrasion", "bandage applied", "Brushed up against metal fence and cut leg")

""" 
                    --- POPULATING THE ZOO ---

The following code will add the above animals, staff, and enclosures to the zoo.
Zoos are used to generate reports from the lists they contain so this is critical.

"""








zac.enclosure = enclosure
maddy.enclosure = enclosure_2
maddy.enclosure = enclosure

enclosure.occupants = allan
enclosure.occupants = bessy
enclosure.occupants = marlin
enclosure.remove_occupant(marlin)
enclosure_4.occupants = fergus


enclosure.clean_enclosure(tom)

tom.add_animal(bessy)

tom.feed_animal(bessy)

adelaide_zoo.add_staff(monica)
adelaide_zoo.add_staff(jimmy)
adelaide_zoo.add_staff(reece)

adelaide_zoo.report_staff()


print(bessy.get_health_record())
print(marlin.get_health_record())