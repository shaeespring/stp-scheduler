import datetime
from buckets import Buckets
from student import Student
def available_times():
    ## Eventually, times will be replaced by variable names given by csv (not available yet)
    # 
    classes ={
              "BReading": ["8am", "9:15", "10:30"],
              "IReading": ["8am", "9:15", "10:30"],
              "AReading": ["8am", "9:15", "10:30"],
              "BMath": ["9:15", "10:30", "1:00"],
              "IMath": ["9:15", "10:30", "1:00"],
              "AMath": ["9:15", "10:30", "1:00"],
              "BASL": ["10:30", "1:00", "2:15"],
              "IASL": ["10:30", "1:00", "2:15"],
              "AASL": ["10:30", "1:00", "2:15"],
              "Presentations": ["1:00", "2:15","3:30"],
              "Lunch" : ["11:45"],
              "Mentoring": ["8am", "9:15am", "2:15"]
              }
    # using the above dictionary, create a new dict using time objects
    available_times = {}
    for key in classes:
        for time in classes[key]:
            available_times[datetime.datetime.strptime(time, "%I:%M%p")] = key


def assignment(student: Student):
    ## English
    if student.english == beginner:
        NAN = 0
        ##choose one BReading time
        #class cannot be full
        ##time cannot be taken on the students schedule
    elif student.english == intermediate:
        NAN = 1
        ##choose one IReading time
        #class cannot be full
        ##time cannot be taken on the students schedule
    elif student.english == advanced:
        NAN = 2
        ##choose one AReading time
        #class cannot be full
        ##time cannot be taken on the students schedule

        ## Math
    if student.math == beginner:
        NAN = 0
        ##choose one BMath time
        #class cannot be full
        ##time cannot be taken on the students schedule
    elif student.math == intermediate:
        NAN = 1
        ##choose one IMath time
        #class cannot be full
        ##time cannot be taken on the students schedule
    elif student.math == advanced:
        NAN = 2
        ##choose one AMath time
        #class cannot be full
        ##time cannot be taken on the students schedule

    ## ASL
    if student.ASL == beginner:
        NAN = 0
        ##choose one BASL time
        #class cannot be full
        ##time cannot be taken on the students schedule
    elif student.ASL == intermediate:
        NAN = 1
        ##choose one IASL time
        #class cannot be full
        ##time cannot be taken on the students schedule
    elif student.ASL == advanced:
        NAN = 2
        ##choose one AASL time
        #class cannot be full
        ##time cannot be taken on the students schedule

    ##choose one presentation time
    ##choose one mentoring time
    ##all students will have lunch at 11:45
        
        


## Students need ONE CLASS from EACH SUBJECT 