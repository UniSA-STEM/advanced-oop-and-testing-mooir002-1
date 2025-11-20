"""
File: zoo.py
Description: A brief description of this Python module.
Author: Isaac Moore
ID: 110117290
Username: mooir002
This is my own work as defined by the University's Academic Integrity Policy.
"""



class Zoo:

    def __init__(self, name:str):

        if not isinstance(name, str):
            raise TypeError("name must be a string")

        self.__name = name
        self.__staff = []
        self.__animals = []
        self.__enclosures = []

    def get_name(self):
        return self.__name

    name = property(get_name)

    def get_staff(self):
        return self.__staff

    def add_staff(self, staff):
        from staff import Staff
        if not isinstance(staff, Staff):
            raise TypeError("staff must be of type Staff")
        self.__staff.append(staff)

    def report_staff(self):
        print(f"| STAFF LIST - {self.name} |\n")
        report = ""
        counter = 1
        for x in self.__staff:
            report += (f"| STAFF MEMBER {counter} |\n ID: {x.staff_id}\n NAME: {x.name}\n ROLE: {x.__class__.__name__.lower()}\n\n")
            counter += 1
        print(report)