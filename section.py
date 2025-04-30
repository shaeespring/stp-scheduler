class Section:
    """ 
    Creates a section of a class that students will take
    Name: Name of the Class, could be seperated into 'name, difficulty'
    Time: Available times of the class
    Capacity: How many students can take the class
    """
    def __init__(self, subject, time, capacity, level, teacher):
        self.__subject = subject
        self.__time = time
        self.__cap = capacity
        self.__current_students = 0
        self.__level = level
        self.__teacher = teacher

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
    def add_student(self):
        if self.is_full():
            return IndexError
        else:
            self.__current_students += 1

    def set_teacher(self,teacher):
        self.__teacher = teacher
    
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
        
    