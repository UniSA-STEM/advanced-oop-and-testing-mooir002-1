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
record = HealthRecord(213, tiko, {})
entry = HealthEntry("Tiko is looking good", "N/A", datetime.datetime.now(), tiko)
entry2 = HealthEntry("Tiko is feeling unwell", "Panadol", datetime.datetime.now(), tiko)
entry3 = HealthEntry("Tiko is much improved", "N/A", datetime.datetime.now(), tiko)

record.add_entry(entry)
record.add_entry(entry2)
record.add_entry(entry3)
print(record.entries)
print(entry)
print(entry2)
print(entry3)