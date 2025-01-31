import datetime

from classes.TimestampParser import TimestampParser
from enums import IOType

class IOEvent:
    def __init__(self, text: str, type: IOType, time: str):
        self._text: str = text
        self._type: IOType = type
        self._time: datetime = TimestampParser.parse_timestamp_str(time)
    
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