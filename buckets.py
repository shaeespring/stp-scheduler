from student import Student

class Buckets:
    #3 lists for each of the three types
    #begining intermediate high
    #1. english
    #2. math
    #3. ASL
    #listed in priorty order. 
    # this assumes a list sorted by name, english, math, asl is students.
    beginningEnglish: list = []
    intermediateEnglish: list = []
    advancedEnglish: list = []

    beginningMath: list = []
    intermediateMath: list = []
    advancedMath: list = []

    beginningASL: list = []
    intermediateASL: list = []
    advancedASL: list = []
    
    
    def sortcourses(self, students: object):
        
        for student in students:    
            # Put into proper Enlish bucket
            if student.english <= 4:
                self.beginningEnglish.append(student)
            elif student.math >= 8:
                self.advancedEnglish.append(student)
            else:
                self.intermediateEnglish.append(student)

            # Put into proper Math bucket
            if student.math <= 4:
                self.beginningMath.append(student)
            elif student.math >= 8:
                self.advancedMath.append(student)
            else:
                self.intermediateMath.append(student)
            
            #put into proper ASL bucket. 
            if student.asl <= 4:
                self.beginningASL.append(student)
            elif student.asl >= 8:
                self.advancedASL.append(student)
            else:
                self.intermediateASL.append(student)
        