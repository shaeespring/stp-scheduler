from typing import Dict, List, Tuple, Union
from section import Section

class Student:
 
    def __init__(self, name, english, math, asl):
        self.name = name
        self.english = english 
        self.math = math
        self.asl = asl
        self.schedule = []
        self.time_blocks = []

    def is_full(self) -> bool:
        """
        Checks if the student's schedule is full.
        """
        return len(self.schedule) >= 6

    def get_english_level(self) -> int:
        """Returns the student's English level"""
        return 0 if self.english <= 3 else 2 if self.english > 6 else 1
    
    def get_math_level(self) -> int:
        """Returns the student's Math level"""
        return 0 if self.math <= 3 else 2 if self.math > 6 else 1
    
    def get_asl_level(self) -> int:
        """Returns the student's ASL level"""
        return 0 if self.asl <= 3 else 2 if self.asl > 6 else 1
    
    def add_section(self, course: Section):
        """Adds a class to the student's schedule"""
        # Check if the course is already in the schedule
        for section in self.schedule:
            if section == course:
                return
        self.schedule.append(course)
        self.add_time_block(course.get_time())

    def add_time_block(self, time_block):
        """Adds a time block to the student's schedule"""
        self.time_blocks.append(time_block)
    
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
    
    def __hash__(self):
        return hash((self.name, self.english, self.math, self.asl))
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.english == other.english and self.math == other.math and self.asl == other.asl
        return False
    
    def __repr__(self):
        return self.__str__()
    
