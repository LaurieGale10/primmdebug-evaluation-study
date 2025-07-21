import datetime

from analysis.log_data_analysis.classes.timestamp_parser import TimestampParser

class ChangePaneContentEvent:
    def __init__(self, new_content: str, time: str):
        self._new_content: str = new_content
        self._time: datetime = TimestampParser.parse_timestamp_str(time)

    @property
    def new_content(self) -> str:
        return self._new_content
    
    @property
    def time(self) -> str:
        return self._time
    
    @staticmethod
    def parse_pane_content_change_log(raw_logs: dict) -> 'ChangePaneContentEvent':
        return ChangePaneContentEvent(
            new_content = raw_logs["newContent"],
            time = raw_logs["time"]
        )
        
    def __repr__(self) -> str:
        return f'ChangePaneContentEvent(\'{self._new_content}\', {self._time})'