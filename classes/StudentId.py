class StudentId:
    def __init__(self, id: str, school: str, date_first_accessed = None):
        self._id = id
        self._school = school
        self._date_first_accessed = date_first_accessed

    @property
    def id(self):
        return self._id
    
    @property
    def school(self):
        return self._school
    
    @property
    def date_first_accessed(self):
        return self._date_first_accessed