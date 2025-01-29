from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from classes.TimestampParser import TimestampParser
from enums import FocusType

class WindowFocusEvent:
    def __init__(self, focus: FocusType, time: DatetimeWithNanoseconds):
        self._focus: FocusType = focus
        self._time: str = int(time.timestamp())

    @property
    def focus(self) -> FocusType:
        return self._focus
    
    @property
    def time(self) -> str:
        return self._time
    
    def __repr__(self):
        return f'WindowFocusEvent({self._focus}, {self._time})'