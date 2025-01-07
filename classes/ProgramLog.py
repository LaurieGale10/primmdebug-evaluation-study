from classes.IOEvent import IOEvent


class ProgramLog:
    def __init__(self, snapshot: str, timestamp, compiled: bool, io_events: list[IOEvent] = None):
        self._snapshot = snapshot
        self._timestamp = timestamp
        self._compiled = compiled
        self._io_events = io_events
    
    @property
    def snapshot(self) -> str:
        return self._snapshot

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def compiled(self) -> bool:
        return self._compiled

    @property
    def io_events(self) -> list[IOEvent]:
        return self._io_events