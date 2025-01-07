from enums import IOType

class IOEvent:
    def __init__(self, text: str, type: IOType, time):
        self._text = text
        self._type = type
        self._time = time
    
    @property
    def text(self) -> str:
        return self._text

    @property
    def type(self) -> IOType:
        return self._type

    @property
    def time(self):
        return self._time