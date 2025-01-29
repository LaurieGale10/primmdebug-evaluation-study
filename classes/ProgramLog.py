from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from classes.IOEvent import IOEvent
from classes.TimestampParser import TimestampParser


class ProgramLog:
    def __init__(self, snapshot: str, timestamp: DatetimeWithNanoseconds, compiled: bool, io_events: list[IOEvent]):
        self._snapshot: str = snapshot
        self._timestamp: str = int(timestamp.timestamp())
        self._compiled: bool = compiled
        self._io_events: list[IOEvent] = io_events
    
    @property
    def snapshot(self) -> str:
        return self._snapshot

    @property
    def timestamp(self) -> str:
        return self._timestamp

    @property
    def compiled(self) -> bool:
        return self._compiled

    @property
    def io_events(self) -> list[IOEvent]:
        return self._io_events
    
    def __repr__(self):
        return f'ProgramLog(\'{self._snapshot}\', {self._timestamp}, {self._compiled}, {self._io_events})'