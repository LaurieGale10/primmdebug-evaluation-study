import datetime

from classes.TimestampParser import TimestampParser
from enums import PaneView


class TogglePaneExpansionEvent:
    def __init__(self, new_pane_view: PaneView, time: str):
        self._new_pane_view: PaneView = new_pane_view
        self._time: datetime = TimestampParser.parse_timestamp_str(time)
    
    @property
    def new_pane_view(self) -> PaneView:
        return self._new_pane_view

    @property
    def time(self) -> str:
        return self._time
    
    @staticmethod
    def parse_pane_expansion_log(raw_logs: dict) -> 'TogglePaneExpansionEvent':
        return TogglePaneExpansionEvent(
            new_pane_view = PaneView[raw_logs["newPaneView"]],
            time = raw_logs["time"]
        )
        
    def __repr__(self):
        return f'TogglePaneExpansionEvent({self._new_pane_view}, {self._time})'