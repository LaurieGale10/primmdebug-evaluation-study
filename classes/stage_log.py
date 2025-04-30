import datetime

from classes.hint_pane_log import HintPaneLog
from classes.program_log import ProgramLog
from classes.test_case_log import TestCaseLog
from classes.window_focus_event import WindowFocusEvent
from classes.timestamp_parser import TimestampParser
from enums import DebuggingStage

class StageLog:
    def __init__(self, id: str, time: str, stage_string: str, program_logs: list[ProgramLog] = None, response: str = None, correct: bool = None, focus_events: list[WindowFocusEvent] = None, test_case_logs: TestCaseLog = None, hint_pane_logs: HintPaneLog = None):
        self._id : str= id
        if stage_string == "exit":
            self._stage_name: DebuggingStage = DebuggingStage("exit")
            self._time: datetime = TimestampParser.parse_timestamp_str(time)
        else:
            self._end_time: datetime = TimestampParser.parse_timestamp_str(time)
            self._overall_stage_number: int = int(stage_string.split("_")[0])
            self._stage_iteration: int = int(stage_string.split("_")[len(stage_string.split("_")) - 1])
            self._stage_name: DebuggingStage = DebuggingStage("_".join(stage_string.split("_")[1:-1]))
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
    
    @property
    def start_time(self) -> datetime:
        return self._start_time if self._start_time is not None else None
    
    @property
    def end_time(self) -> datetime:
        return self._end_time
    
    def reconstruct_stage_string(self) -> str:
        return f"{self._overall_stage_number}_{self._stage_name}_{self._stage_iteration}"

    @property
    def overall_stage_number(self) -> int:
        return self._overall_stage_number if self._overall_stage_number is not None else None

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

    @focus_events.setter
    def focus_events(self, focus_events: list[WindowFocusEvent]):
        self._focus_events = focus_events

    @property
    def test_case_logs(self) -> TestCaseLog:
        return self._test_case_logs

    @property
    def hint_pane_logs(self) -> str:
        return self._hint_pane_logs
    
    @staticmethod
    def parse_stage_log(raw_logs: dict) -> 'StageLog':
        #Parse program logs, window focus events, test case logs, and hint pane logs
        parsed_program_logs = None
        if "programLogs" in raw_logs:
            parsed_program_logs = []
            for raw_program_log in raw_logs["programLogs"]:
                parsed_program_logs.append(ProgramLog.parse_program_log(raw_program_log))
        
        parsed_window_focus_events = None
        if "focusEvents" in raw_logs:
            parsed_window_focus_events = []
            for raw_window_focus_event in raw_logs["focusEvents"]:
                parsed_window_focus_events.append(WindowFocusEvent.parse_window_focus_event(raw_window_focus_event))
        
        parsed_test_case_log = None
        if "testCaseLogs" in raw_logs:
            parsed_test_case_log = TestCaseLog.parse_test_case_log(raw_logs["testCaseLogs"])
        
        parsed_hint_pane_log = None
        if "hintPaneLogs" in raw_logs:
            parsed_hint_pane_log = HintPaneLog.parse_hint_pane_log(raw_logs["hintPaneLogs"])
        return StageLog(
            id = raw_logs["id"],
            time = raw_logs["time"],
            stage_string = raw_logs["stage"],
            program_logs = parsed_program_logs,
            response = raw_logs.get("response"),
            correct = raw_logs.get("correct"),
            focus_events = parsed_window_focus_events,
            test_case_logs = parsed_test_case_log,
            hint_pane_logs = parsed_hint_pane_log
    )
    
    def __repr__(self):
        if self._stage_name.value == "exit":
            return f'StageLog(\'{self._id}\', {self._time}, \'{self._stage_name}\')'
        return f'StageLog(\'{self._id}\', {self._end_time}, \'{self._overall_stage_number}\', \'{self.stage_name}\', \'{self._stage_iteration}\', {self._program_logs}, \'{self._response}\', {self._correct}, {self._focus_events}, {self._test_case_logs}, {self._hint_pane_logs})'