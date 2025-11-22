"""
File: main.py
Description: This is where all the main code shall run
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports all required modules into main

from animal import *
from enclosure import *
from staff import *
from zoo import *
from health_entries import *
import datetime

"""                --- CREATION OF OBJECTS & INSTANCES ---

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

entry_1 = BehaviouralConcern(jimmy, datetime.datetime.now(), bessy, "depression", "sitting in corner not usual self", "socialise with other chimps")
entry_2 = Injury(reece, datetime.datetime.now(), bessy, "sprained ankle", "rest, ice, compression", "fell out of tree")
entry_3 = Illness(monica, datetime.datetime.now(), bessy, "migraine", "asprin", "isolate in dark room away from lights and sounds")
entry_4 = BehaviouralConcern(jimmy, datetime.datetime.now(), bessy, "play", "playing happily with other chimps", "back to her normal self again")

entry_5 = Injury(monica, datetime.datetime.now(), becky, "broken wing", "cast", "flew into a wall")
entry_6 = Illness(monica, datetime.datetime.now(), becky, "infection", "antibiotics", "wing has become infected")
entry_7 = Illness(jimmy, datetime.datetime.now(), becky, "fever", "paracetamol", "infection has spread further - 20min continuous observation required")
entry_8 = BehaviouralConcern(jimmy, datetime.datetime.now(), becky, "hallucinations", "squarking at nothing as if there was a threat", "keep fever down with paracetamol - ice bath if required")

entry_9 = Illness(monica, datetime.datetime.now(), allan, "stomach ache", "n/a", "observe overnight for change in symptoms")
entry_10 = BehaviouralConcern(jimmy, datetime.datetime.now(), allan, "aggression", "attempted to bite keeper", "leave alone for 24hrs")
entry_11 = Injury(reece, datetime.datetime.now(), allan, "abrasion", "bandage applied", "Brushed up against metal fence and cut leg")
entry_12 = BehaviouralConcern(monica, datetime.datetime.now(), allan, "aggression", "attempted to bite keeper... again", "leave alone for 48hrs")

entry_13 = BehaviouralConcern(reece, datetime.datetime.now(), fergus, "lethargic", "not responding to external stimuli or food", "place under observation")
entry_14 = Injury(reece, datetime.datetime.now(), fergus, "blocked gut", "surgery", "gut is blocked - ate something he shouldn't have needs to be removed")
entry_15 = Illness(monica, datetime.datetime.now(), fergus, "migrane", "asprin", "isolate in dark room away from lights and sounds")
entry_16 = BehaviouralConcern(jimmy, datetime.datetime.now(), fergus, "eating", "ate a small number of meal worms", "has regained appetite - seems to be on the mend")

entry_17 = Injury(jimmy, datetime.datetime.now(), marlin, "cut fin", "switches", "swam into sharp rock - needed 4 stitches")
entry_18 = Illness(monica, datetime.datetime.now(), marlin, "infection", "antibiotics", "fin has become infected")
entry_19 = Illness(jimmy, datetime.datetime.now(), marlin, "secondary infection", "antibiotics (higher dose)", "infection has not reduced - have upped the dose")
entry_20 = BehaviouralConcern(reece, datetime.datetime.now(), marlin, "unusual behaviour", "swimming around in circles", "keep an eye on him - may not be fully recovered")


"""                     --- POPULATING THE ZOO ---

The following code will add the above animals, staff, and enclosures to the zoo.
Zoos are used to generate reports from the lists they contain so this is a critical step.

"""

# adds staff to the zoo

adelaide_zoo.add_staff(zac)
adelaide_zoo.add_staff(maddy)
adelaide_zoo.add_staff(tom)
adelaide_zoo.add_staff(sarah)
adelaide_zoo.add_staff(reece)
adelaide_zoo.add_staff(monica)
adelaide_zoo.add_staff(jimmy)

# adds enclosures to the zoo

adelaide_zoo.add_enclosure(enclosure)
adelaide_zoo.add_enclosure(enclosure_2)
adelaide_zoo.add_enclosure(enclosure_3)
adelaide_zoo.add_enclosure(enclosure_4)
adelaide_zoo.add_enclosure(enclosure_5)

# adds animals to the zoo

adelaide_zoo.add_animal(bessy)
adelaide_zoo.add_animal(becky)
adelaide_zoo.add_animal(allan)
adelaide_zoo.add_animal(fergus)
adelaide_zoo.add_animal(marlin)

"""         --- SETTING UP THE ENCLOSURES ---

The following code will add animals to enclosures
It will also assign staff members to oversee each enclosure

"""

# add zoo animals to an enclosure

enclosure.occupant = bessy
enclosure.occupant = becky
enclosure_3.occupant = marlin
enclosure_4.occupant = fergus
enclosure_5.occupant = allan

# add zoo keepers to specific enclosures. Each keeper is responsible for at least 2 enclosures

zac.enclosure = enclosure
zac.enclosure = enclosure_3
maddy.enclosure = enclosure_2
maddy.enclosure = enclosure
sarah.enclosure = enclosure_3
sarah.enclosure = enclosure_4
tom.enclosure = enclosure_5
tom.enclosure = enclosure_2

"""         --- HEALTH SYSTEM FUNCTIONALITY ---

The following reports all relate to animal health records and their entries

"""

# prints a summary of a specific animal's health record
# how many entries do they have etc...

bessy.print_health_record()

# prints every single entry from a specific animal's health record
# includes specific details from each entry such as what the issue was.

marlin.print_all_entries()

# prints a details list of the specific categories of entries from a health record
# includes specific details from each entry such as what the issue was.

allan.print_behavioural_entries()
becky.print_injury_entries()
fergus.print_illness_entries()

# removes a specific health entry from an animal's health record

allan.health_record.remove_entry(0)
becky.health_record.remove_entry(2)

# vets can diagnose animals as sick or well - this updates their health record

jimmy.diagnose_sick(bessy)
reece.diagnose_well(bessy)

# vets can also diagnose animals as injured or healed - this updates their health record

reece.diagnose_injured(bessy)
monica.diagnose_healed(bessy)

"""     --- OTHER ZOO FUNCTIONALITY ---     

- Removing animals, staff, enclosures
- Report on enclosures, staff and animals
- Report on species

"""

# removes a specific staff member from the zoo

adelaide_zoo.remove_staff(jimmy)

# removes a specific animal from the zoo

adelaide_zoo.remove_animal(marlin)

# removes a specific enclosure from the zoo

adelaide_zoo.remove_enclosure(enclosure)

# generate a report on all the enclosures within the zoo

adelaide_zoo.report_enclosures()

# generate a report on all the staff within the zoo

adelaide_zoo.report_staff()

# generate a report on all the animals within the zoo

adelaide_zoo.report_animals()

# generates are report of all the different species of animals in the zoo

adelaide_zoo.report_species()

adelaide_zoo.report_categories()
