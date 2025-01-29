from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from classes import HintPaneLog
from classes.ProgramLog import ProgramLog
from classes.TestCaseLog import TestCaseLog
from classes.WindowFocusEvent import WindowFocusEvent
from classes.TimestampParser import TimestampParser
from enums import DebuggingStage

class StageLog:
    def __init__(self, id: str, time: DatetimeWithNanoseconds, stage_string: str, program_logs: list[ProgramLog] = None, response: str = None, correct: bool = None, focus_events: list[WindowFocusEvent] = None, test_case_logs: TestCaseLog = None, hint_pane_logs: HintPaneLog = None):
        self._id : str= id
        self._time: int = int(time.timestamp()),
        if stage_string == "exit":
            self._stage_name: str = "exit"
        else:
            self._overall_stage_number: int = stage_string.split("_")[0]
            self._stage_iteration: int = stage_string.split("_")[2]
            self._stage_name: str = stage_string.split("_")[1] #Could convert to an enum here?
        #TODO: Perform null checks here
        self._program_logs: list[ProgramLog] = program_logs
        self._response: str = response
        self._correct: bool = correct
        self._focus_events: list[WindowFocusEvent] = focus_events
        self._test_case_logs: TestCaseLog = test_case_logs
        self._hint_pane_logs: HintPaneLog = hint_pane_logs

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def time(self) -> str:
        return self._time
    
    def reconstruct_stage_string(self) -> str:
        return f"{self._overall_stage_number}_{self._stage_name}_{self._stage_iteration}"

    @property
    def overall_stage_number(self) -> int:
        return self._overall_stage_number

    @property
    def stage_iteration(self) -> int:
        return self._stage_iteration

    @property
    def stage_name(self) -> DebuggingStage:
        return self._stage_name

    @property
    def program_logs(self) -> list[ProgramLog]:
        return self._program_logs

    @property
    def response(self) -> str:
        return self._response

    @property
    def correct(self) -> bool:
        return self._correct

    @property
    def focus_events(self) -> list[WindowFocusEvent]:
        return self._focus_events

    @property
    def test_case_logs(self) -> TestCaseLog:
        return self._test_case_logs

    @property
    def hint_pane_logs(self) -> str:
        return self._hint_pane_logs
    
    def __repr__(self):
        if self._stage_name == "exit":
            return f'StageLog(\'{self._id}\', {self._time}, \'{self._stage_name}\')'
        return f'StageLog(\'{self._id}\', {self._time}, \'{self._overall_stage_number}\', \'{self.stage_name}\', \'{self._stage_iteration}\', {self._program_logs}, \'{self._response}\', {self._correct}, {self._focus_events}, {self._test_case_logs}, {self._hint_pane_logs})'