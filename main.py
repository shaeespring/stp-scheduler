""" Priority Scheduler: 

1. Schedule each student by the lowest test score first 
2. If not, schedule in this order:
    - English
    - Math
    - ASL

"""
from typing import Dict, List, Tuple, Union
from math import average
import os
from student import Student

def load_csv(file_name) -> List[Student]:
    """
    CSV Format: 
    Name, Reading, Writing, Math, ASL

    Returns:
    {
        "Name": {
            "English": int,
            "Math": int,
            "ASL": int
        }
    }
    """
    with open(file_name, 'r') as file:
        data = file.readlines()
    data = [line.strip().split(',') for line in data]
    students_to_score = [Student(line[0], (int(line[1]) +  int(line[2])) // 2, int(line[3]), int(line[4])) for line in data]
    return students_to_score

def return_scores(students_to_score: List[Student]) -> List[Student]:
    """
    Returns a list of test scores for each student.
    """
    return [(student_to_score.english, student_to_score.math, student_to_score.asl) for student_to_score in students_to_score]

def sort_students(students_to_score: List[Student]) -> List[Student]:
    """
    Returns a list of student names in the order they should be scheduled.
    """
    sorted_students = sorted(students_to_score, key=(min(return_scores(students_to_score)), return_scores(students_to_score)))
    return sorted_students
