from enums import FocusType

class WindowFocusEvent:
    def __init__(self, focus: FocusType, time):
        self._focus = focus
        self._time = time

    @property
    def focus(self) -> FocusType:
        return self._focus
    
    @property
    def time(self):
        return self._time
    
    def __repr__(self):
        return f'WindowFocusEvent({self._focus}, {self._time})'