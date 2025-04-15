from typing import Dict, List, Tuple, Union

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
    
    def add_class(self, course):
        self.schedule.append(course)
    
    def remove_class(self, course):
        self.schedule.remove(course)
    
    def get_schedule(self):
        return self.schedule
    
    # ???
    # def return_scores(self,students_to_score: List[Student]) -> List[Student]:
    #     """
    #     Returns a list of test scores for each student.
    #     """
    #     return [(student_to_score.english, student_to_score.math, student_to_score.asl) for student_to_score in students_to_score]