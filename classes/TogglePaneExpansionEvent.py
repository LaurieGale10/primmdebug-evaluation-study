from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from classes.TimestampParser import TimestampParser
from enums import PaneView


class TogglePaneExpansionEvent:
    def __init__(self, new_pane_view: PaneView, time: DatetimeWithNanoseconds):
        self._new_pane_view: PaneView = new_pane_view
        self._time: str = int(time.timestamp())
    
    @property
    def new_pane_view(self) -> PaneView:
        return self._new_pane_view

    @property
    def time(self) -> str:
        return self._time
    
    def __repr__(self):
        return f'TogglePaneExpansionEvent({self._new_pane_view}, {self._time})'