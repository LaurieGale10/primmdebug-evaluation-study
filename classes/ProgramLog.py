import datetime

from classes.IOEvent import IOEvent
from classes.TimestampParser import TimestampParser


class ProgramLog:
    def __init__(self, snapshot: str, timestamp: str, compiled: bool, io_events: list[IOEvent]):
        self._snapshot: str = snapshot
        self._timestamp: datetime = TimestampParser.parse_timestamp_str(timestamp)
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
    
    @staticmethod
    def parse_program_log(raw_log: dict) -> 'ProgramLog':
        parsed_io_events = []
        for raw_io_event in raw_log["io"]:
            parsed_io_events.append(IOEvent.parse_io_event(raw_io_event))
            return ProgramLog(
                snapshot = raw_log["snapshot"],
                timestamp = raw_log["timestamp"],
                compiled = raw_log["compiled"],
                io_events = parsed_io_events
            )
        
    def __repr__(self):
        return f'ProgramLog(\'{self._snapshot}\', {self._timestamp}, {self._compiled}, {self._io_events})'