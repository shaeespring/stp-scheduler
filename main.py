""" Priority Scheduler: 

1. Schedule each student by the lowest test score first 
2. If not, schedule in this order:
    - English
    - Math
    - ASL

A score of 0 means that no test score was received. In this instance, they will default to Beginner level.
"""
from typing import List, Tuple
from student import Student
from buckets import Buckets
from teacher import Teacher

def load_student_csv(file_name) -> List[Student]:
    """
    CSV Format: 
    Name, English, Math, ASL
    """
    with open(file_name, 'r') as file:
        data = file.readlines()
    data = [line.strip().split(',') for line in data]
    students = []
    
    for i, line in enumerate(data):
        if i == 0:
            continue
        if line[0] == '':
            line[0] = 'Unknown'
        if line[1] == '':
            line[1] = 0
        if line[2] == '':
            line[2] = 0
        if line[3] == '':
            line[3] = 0
        
        name = line[0]
        english = int(line[1])
        math = int(line[2])
        asl = int(line[3])
        students.append(Student(name, english, math, asl))
    
    return students

def return_scores(students: List[Student]) -> List[Tuple[int, int, int]]:
    """
    Returns a list of test scores for each student.
    """
    return [(student_to_score.english, student_to_score.math, student_to_score.asl) for student_to_score in students]

def make_buckets(students: List[Student]) -> Buckets:
    bucket = Buckets()
    bucket.sortcourses(students)
    return bucket
    
def sort_students(students_to_score: List[Student]) -> List[Student]:
    """
    Returns a list of student names in the order they should be scheduled.
    """
    sorted_students = sorted(students_to_score, key=(min(return_scores(students_to_score)), return_scores(students_to_score)))
    return sorted_students

def load_instructor_csv(file_name) -> List[Teacher]:
    """
    CSV Format:
    Course, Instructor, Section Count, Blank Space, Mentoring Info
    """
    with open(file_name, 'r') as file:
        data = file.readlines()
    data = [line.strip().split(',') for line in data]
    instructors = []
    mentors = []
    for i, line in enumerate(data):
        if i == 0:
            continue
        
        if line[4] != '':
            mentors.append(line[4])
        
        if line[0] == '':
            continue
        if line[1] == '':
            line[1] = 'TBD'
        if line[2] == '':
            line[2] = 1
        instructors.append(line[0: 3])
    
    teachers = []
    for instructor in instructors:
        if instructor[1] not in mentors:
            teachers.append(Teacher(*instructor))
        else:
            mentors.remove(instructor[1])
            teachers.append(Teacher(*instructor, is_mentor=True))
    if len(mentors) > 0:
        for mentor in mentors:
            teachers.append(Teacher('Mentoring', mentor, 0, is_mentor=True))
    return teachers



def main():
    # Load the CSV files
    students = load_student_csv('students.csv')
    instructors = load_instructor_csv('instructors.csv')
    
    # Create buckets for each subject
    buckets = make_buckets(students)
    
    # Print the students and their buckets
    print(len(students), "students loaded.")
    print(buckets)
    
    # Print instructors and classes
    print(len(instructors), "instructors loaded.")
    for instructor in instructors:
        print(instructor)
    
def test_instructors():
    instructors = load_instructor_csv('instructors.csv')
    for instructor in instructors:
        print(instructor)

        
if __name__ == "__main__":
    main()