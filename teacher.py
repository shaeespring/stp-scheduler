class Teacher:
    def __init__(self, subject, name, sections, is_mentor=False):
        self.name = name
        self.subject = subject
        self.sections = int(sections)
        self.is_mentor = is_mentor
        self.schedule = []
        self.time_blocks = []
    
    def is_full(self):
        """
        Checks if the teacher's schedule is full.
        """
        return len(self.schedule) >= self.sections

    def add_section(self, section):
        """
        Adds a section to the teacher's schedule.
        """
        if self.is_full():
            raise IndexError("Teacher's schedule is full.")
        else:
            self.schedule.append(section)

    def add_time_block(self, time_block):
        """
        Adds a time block to the teacher's schedule.
        """
        self.time_blocks.append(time_block)
    
    def __str__(self):
        return f"{self.name} ({self.subject}) - {self.sections} sections{' (Mentor)' if self.is_mentor else ''}"
    
    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash((self.name, self.subject, self.sections, self.is_mentor))
    
    def __eq__(self, other):
        if isinstance(other, Teacher):
            return self.name == other.name and self.subject == other.subject and self.sections == other.sections and self.is_mentor == other.is_mentor
        return False