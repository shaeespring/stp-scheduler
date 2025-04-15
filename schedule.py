import datetime
from buckets import Buckets
from student import Student
import random
import classes

## Eventually, times will be replaced by variable names given by csv (not available yet)
#

# BReading = classes("BReading", ["8am", "9:15", "10:30"], 20)
# IReading = classes("IReading", ["8am", "9:15", "10:30"], 20)
# AReading = classes("AReading", ["8am", "9:15", "10:30"], 20)
# BMath = classes("BMath", ["9:15", "10:30", "1:00"], 20)
# IMath = classes("IMath", ["9:15", "10:30", "1:00"], 20)
# AMath = classes("AMath", ["9:15", "10:30", "1:00"], 20)
# BASL = classes("BASL", ["10:30", "1:00", "2:15"], 20)
# IASL = classes("IASL", ["10:30", "1:00", "2:15"], 20)
# AASL = classes("AASL", ["10:30", "1:00", "2:15"], 20)
# Presentations = classes("Presentations", ["1:00", "2:15", "3:30"], 20)
# Lunch = classes("Lunch", ["11:45"], 100000)
# Mentoring = classes("Mentoring", ["8am", "9:15am", "2:15"], 20)


def assignment(student: Student):
    ## English
    if student.english == "beginner":
        NAN=0
        ##choose one BReading time
        # class cannot be full
        ##time cannot be taken on the students schedule
    elif student.english == "intermediate":
        NAN = 1
        ##choose one IReading time
        # class cannot be full   I
        ##time cannot be taken on the students schedule
    elif student.english == "advanced":
        NAN = 0
        ##choose one AReading time
        # class cannot be full
        ##time cannot be taken on the students schedule

        ## Math
    if student.math == "beginner":
        NAN = 0
        ##choose one BMath time
        # class cannot be full
        ##time cannot be taken on the students schedule
    elif student.math == "intermediate":
        NAN = 1
        ##choose one IMath time
        # class cannot be full
        ##time cannot be taken on the students schedule
    elif student.math == "advanced":
        NAN = 2
        ##choose one AMath time
        # class cannot be full
        ##time cannot be taken on the students schedule

    ## ASL
    if student.ASL == "beginner":
        NAN = 0
        ##choose one BASL time
        # class cannot be full
        ##time cannot be taken on the students schedule
    elif student.ASL == "intermediate":
        NAN = 1
        ##choose one IASL time
        # class cannot be full
        ##time cannot be taken on the students schedule
    elif student.ASL == "advanced":
        NAN = 2
        ##choose one AASL time
        # class cannot be full
        ##time cannot be taken on the students schedule

    ##choose one presentation time
    ##choose one mentoring time
    
    ##all students will have lunch at 11:45


## Students need ONE CLASS from EACH SUBJECT
