class Teacher:
    def __init__(self, subject, name, sections, is_mentor=False):
        self.name = name
        self.subject = subject
        self.sections = int(sections)
        self.is_mentor = is_mentor
        self.schedule = []
    
    def __str__(self):
        return f"{self.name} ({self.subject}) - {self.sections} sections{' (Mentor)' if self.is_mentor else ''}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if isinstance(other, Teacher):
            return self.name == other.name and self.subject == other.subject and self.sections == other.sections and self.is_mentor == other.is_mentor
        return False