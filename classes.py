

class classes:
    #Creates classes that students will take
    #Name: Name of the Class, could be seperated into 'name, difficulty'
    #Times: Available times of the class
    #Capacity: How many students can take the class
    def __init__(self, name, times, capacity):
        self.name = name
        self.times = times
        self.cap = capacity
        self.currentStudents = 0

    #adds a student to the class
    #eventually this could keep track of which students if desired
    #raises index error if class is at capacity 
    #TODO: correct Error type, with handling
    def add_student():
        if is_full():
            raise IndexError("Class Full")
            return
        else:    
            currentStudents += 1
            
    #Checks if the classs is at capacity
    def is_full():
        if currentStudents == capacity:
            return True
        else: 
            return False

