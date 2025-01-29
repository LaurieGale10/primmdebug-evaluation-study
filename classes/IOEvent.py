from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from classes.TimestampParser import TimestampParser
from enums import IOType

class IOEvent:
    def __init__(self, text: str, type: IOType, time: DatetimeWithNanoseconds):
        self._text: str = text
        self._type: IOType = type
        self._time: str = int(time.timestamp())
    
    @property
    def text(self) -> str:
        return self._text

    @property
    def type(self) -> IOType:
        return self._type

    @property
    def time(self) -> str:
        return self._time
    
    @staticmethod
    def parse_io_event(raw_log: dict) -> 'IOEvent':
        return IOEvent(
            text = raw_log["text"],
            type = IOType[raw_log["type"]], #This might not work and might have to do a switch statement,
            time = raw_log["time"]
        )
    
    def __repr__(self):
        return f'IOEvent(\'{self._text}\', {self._type}, {self._time})'