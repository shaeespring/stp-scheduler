""" Priority Scheduler: 

1. Schedule each student by the lowest test score first 
2. If not, schedule in this order:
    - English
    - Math
    - ASL

A score of 0 means that no test score was received. In this instance, they will default to Beginner level.
"""
from typing import List, Tuple, Dict, Union
from student import Student
from buckets import Buckets
from teacher import Teacher
from section import Section
from constants import *
import math


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
    bucket.sort_courses(students)
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

def create_sections_easy(class_count_dict: Dict) -> List[Section]:
    """
    Creates sections for each class assuming there is no issue with the number of students.
    """
    sections = []
    for class_name, count in class_count_dict.items():
        if count > 0:
            for i in range(count):
                level = 0
                if "beginning" in class_name:
                    level = BEGINNER
                elif "intermediate" in class_name:
                    level = INTERMEDIATE
                elif "advanced" in class_name:
                    level = ADVANCED

                if "English" in class_name:
                    name = "Essential Communication"
                elif "Math" in class_name:
                    name = "Technical Math"
                elif "ASL" in class_name:
                    name = "ASL"

                sections.append(Section(name, None, CLASS_LIMIT, level, None))
    return sections

def create_sections_hard(class_count_dict: Dict, subject_availability_dict: Dict, subjects: Union[List, str]) -> Tuple[List[Section], Dict]:
    """
    Creates sections for each class assuming there is an issue with the number of students.
    This function will create sections based on the availability of subjects.
    If there are not enough sections available, it will prioritize lower level classes first, and then move higher classes to the overflow dictionary.
    
    IN FUTURE ITERATIONS, THIS SHOULD INSTEAD PRIORITIZE THE LARGER CLASS FIRST, THEN THE SMALLER CLASS.
   
    """
    sections = []
    overflow_dict = {}
    class_counts = class_count_dict.items()

    if isinstance(subjects, str):
        subjects = [subjects]

    # Loop through each class and add 1 sections until there are no more subjects available
    subject_availability_dict = {key: value for key, value in subject_availability_dict.items() if key in subjects}  # Filter to only include relevant subjects

    while any(subject_availability_dict.values()):  # Continue while there are available subjects
        # print("Subject availability dict: ", subject_availability_dict)
        for class_name, count in class_counts:
            # print("Class name: ", class_name, "Count: ", count)
            if count > 0:
                # Determine the level based on the class name
                level = 0
                if "beginning" in class_name:
                    level = BEGINNER
                elif "intermediate" in class_name:
                    level = INTERMEDIATE
                elif "advanced" in class_name:
                    level = ADVANCED

                name = class_name
                if "English" in class_name or "Communication" in class_name:
                    name = "Essential Communication"
                elif "Math" in class_name:
                    name = "Technical Math"
                elif "ASL" in class_name:
                    name = "ASL"
                
                # Create a section and append it to the list
                sections.append(Section(name, None, CLASS_LIMIT, level, None))
                
                # Decrement the count in subject_availability_dict
                subject_availability_dict[name] -= 1
                # Decrement the count in class_count_dict
                class_count_dict[class_name] -= 1
                # If the count reaches zero, remove it from the dictionary
                if subject_availability_dict[name] <= 0:
                    del subject_availability_dict[name]
                    break
                
        # print(sections)
    
    # Add any remaining counts to overflow_dict
    for class_name, count in class_count_dict.items():
        if count > 0:
            # print("Adding to overflow dict: ", class_name, count)
            overflow_dict[class_name] = count
    
    return sections, overflow_dict


def main():
    # Load the CSV files
    students = load_student_csv('students.csv')
    instructors = load_instructor_csv('instructors.csv')
    
    # Create buckets for each subject
    buckets = make_buckets(students)
    buckets.set_class_count()
    
    # Print the students and their buckets
    print(len(students), "students loaded.")
    print(buckets)
    
    # Print instructors and classes
    print(len(instructors), "instructors loaded.")
    subject_availability_dict = {}
    for instructor in instructors:
        print(instructor)
        subject_availability_dict[instructor.subject] = instructor.sections if not subject_availability_dict.get(instructor.subject) else subject_availability_dict[instructor.subject] + instructor.sections

    print(subject_availability_dict)

    class_count_dict = buckets.get_class_count()

    for class_name, count in class_count_dict.items():
        print(f"{class_name}: {count} sections needed")

    # Generate total counts of each class (both available and required)

    english_required_dict = {key: value for key, value in class_count_dict.items() if "English" in key}
    math_required_dict = {key: value for key, value in class_count_dict.items() if "Math" in key}
    asl_required_dict = {key: value for key, value in class_count_dict.items() if "ASL" in key}

    # Create section objects
    print("Creating sections...")
    if sum(english_required_dict.values()) <= subject_availability_dict.get("Essential Communication", 0):
        english_sections = create_sections_easy(english_required_dict)
        english_overflow = {}
    else:
        # print("Hard english")
        english_sections, english_overflow = create_sections_hard(english_required_dict, subject_availability_dict, "Essential Communication")
    if sum(math_required_dict.values()) <= subject_availability_dict.get("Technical Math", 0):
        math_sections = create_sections_easy(math_required_dict)
        math_overflow = {}
    else:
        # print("Hard math")
        math_sections, math_overflow = create_sections_hard(math_required_dict, subject_availability_dict, "Technical Math")
    if sum(asl_required_dict.values()) <= subject_availability_dict.get("ASL", 0):
        asl_sections = create_sections_easy(asl_required_dict)
        asl_overflow = {}
    else:
        # print("Hard asl")
        asl_sections, asl_overflow = create_sections_hard(asl_required_dict, subject_availability_dict, "ASL")
    
    # Combine all sections into one list
    all_sections = english_sections + math_sections + asl_sections
    all_overflow = {**english_overflow, **math_overflow, **asl_overflow}
    print(all_overflow)
    # Print the sections
    print("Sections created:")
    for section in all_sections:
        print(section)
    

    # Assign classes to the instructors
    for instructor in instructors:
        if instructor.sections > 0:
            for class_name, count in class_count_dict.items():
                if instructor.subject == class_name:

                    instructor.sections -= count
                    break

    
    
def test_instructors():
    instructors = load_instructor_csv('instructors.csv')
    for instructor in instructors:
        print(instructor)

        
if __name__ == "__main__":
    main()