from typing import Tuple
from time_block import TimeBlock
from teacher import Teacher
# from student import Student


class Section:
    """ 
    Creates a section of a class that students will take
    Name: Name of the Class, could be seperated into 'name, difficulty'
    Time: Time block of the class
    Days: Days of the week the class is held in the format: "MTWRF"
    Capacity: How many students can take the class
    """
    def __init__(self, subject: str, time: TimeBlock, days:str, capacity: int, level: int, teacher: Teacher):
        self.__subject = subject
        self.__time = time
        self.__cap = capacity
        self.__current_students = 0
        self.__level = level
        self.__teacher = teacher
        self.__days = days
        self.__students = []

    # Checks if the classs is at capacity
    def is_full(self):
        if self.__current_students == self.__cap:
            return True
        else:
            return False
    
    # adds a student to the class
    # eventually this could keep track of which students if desired
    # raises index error if class is at capacity
    # TODO: correct Error type, with handling
    def add_student(self, student):
        if self.is_full():
            return IndexError("Class is at capacity.")
        else:
            self.__current_students += 1
            self.__students.append(student)

    def get_students(self):
        return self.__students
    
    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)
            self.__current_students -= 1
        else:
            return IndexError("Student not found in class.")

    def set_teacher(self,teacher):
        self.__teacher = teacher
    
    def set_time(self, time: TimeBlock):
        self.__time = time

    def get_capacity(self):
        return self.__cap
    
    def get_days(self):
        return self.__days
    
    def set_days(self, days: str):
        self.__days = days
    
    def get_current_students(self):
        return self.__current_students
    
    def get_teacher(self):
        return self.__teacher

    def get_time(self):
        return self.__time
    
    def get_level(self):
        return self.__level
    
    def get_subject(self):
        return self.__subject
    
    def __eq__(self, other):
        if isinstance(other, Section):
            return self.__subject == other.__subject and self.__time == other.__time and self.__level == other.__level and self.__teacher == other.__teacher
        return False
    
    def __hash__(self):
        return hash((self.__subject, self.__time, self.__level, self.__teacher))
    
    def __str__(self):
        return f"Section({self.__subject}, {self.__time}, {self.__cap}, {self.__level}, {self.__teacher})"
    
    def __repr__(self):
        return self.__str__()
        
    