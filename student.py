from typing import Dict, List, Tuple, Union
from section import Section

class Student:
    '''CSV Format: 
    Name, Reading, Writing, Math, ASL'''

    name = None
    english = None
    math = None
    asl = None
    schedule = None

    def __init__(self, name, english, math, asl):
        self.name = name
        self.english = english 
        self.math = math
        self.asl = asl
        self.schedule = []
    
    def add_class(self, course: Section):
        """Adds a class to the student's schedule"""
        # Check if the course is already in the schedule
        for section in self.schedule:
            if section == course:
                return
        self.schedule.append(course)
    
    def remove_class(self, course: Section):
        """Removes a class from the student's schedule"""
        # Check if the course is in the schedule
        for section in self.schedule:
            if section == course:
                break
            else:
                return
        self.schedule.remove(course)
    
    def get_schedule(self) -> List[Section]:
        """Returns a list of sections that the student is enrolled in"""
        return self.schedule
    
    def __str__(self):
        return f"{self.name}"
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.english == other.english and self.math == other.math and self.asl == other.asl
        return False
    
    def __repr__(self):
        return self.__str__()
    
