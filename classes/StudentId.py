from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from classes.TimestampParser import TimestampParser


class StudentId:
    def __init__(self, id: str, school: str, date_first_accessed: DatetimeWithNanoseconds = None):
        self._id: str = id
        self._school: str = school
        if date_first_accessed:
            self._date_first_accessed: str = int(date_first_accessed.timestamp())

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def school(self) -> str:
        return self._school
    
    @property
    def date_first_accessed(self) -> str:
        return self._date_first_accessed
    
    def __repr__(self):
        return f'StudentId(\'{self._id}\', \'{self._school}\', {self._date_first_accessed})'