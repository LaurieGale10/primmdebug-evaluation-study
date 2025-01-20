from classes.ChangePaneContentEvent import ChangePaneContentEvent
from classes.ExerciseLog import ExerciseLog
from classes.HintPaneLog import HintPaneLog
from classes.IOEvent import IOEvent
from classes.ProgramLog import ProgramLog
from classes.StageLog import StageLog
from classes.StudentId import StudentId
from classes.TestCaseLog import TestCaseLog
from classes.TogglePaneExpansionEvent import TogglePaneExpansionEvent
from classes.WindowFocusEvent import WindowFocusEvent
from enums import IOType, FocusType, PaneView

def parse_exercise_log(raw_exercise_logs: dict, stage_logs: list[StageLog]) -> ExerciseLog:
    return ExerciseLog(
        student_id = raw_exercise_logs["studentId"],
        exercise_name = raw_exercise_logs["exerciseId"],
        stage_logs = stage_logs,
        start_time = raw_exercise_logs["time"]
    )

"""Functions for parsing stage logs"""

def parse_io_event(raw_log: dict) -> IOEvent:
    return IOEvent(
        text = raw_log["text"],
        type = IOType[raw_log["type"]], #This might not work and might have to do a switch statement,
        time = raw_log["time"]
    )

def parse_program_log(raw_log: dict) -> ProgramLog:
    parsed_io_events = []
    for raw_io_event in raw_log["io"]:
        parsed_io_events.append(parse_io_event(raw_io_event))
    return ProgramLog(
        snapshot = raw_log["snapshot"],
        timestamp = raw_log["timestamp"],
        compiled = raw_log["compiled"],
        io_events = parsed_io_events
    )

def parse_window_focus_event(raw_logs: dict) -> WindowFocusEvent:
    return WindowFocusEvent(
        focus = FocusType[raw_logs["focus"]],
        time = raw_logs["time"]
    )

def parse_pane_expansion_log(raw_logs: dict) -> TogglePaneExpansionEvent:
    return TogglePaneExpansionEvent(
        new_pane_view = PaneView[raw_logs["newPaneView"]],
        time = raw_logs["time"]
    )

def parse_pane_content_change_log(raw_logs: dict) -> ChangePaneContentEvent:
    return ChangePaneContentEvent(
        new_content = raw_logs["newContent"],
        time = raw_logs["time"]
    )

def parse_test_case_log(raw_logs: dict) -> TestCaseLog:
    if (raw_logs["expansionChanges"]):
        parsed_expansion_changes = []
        for raw_expansion_change in raw_logs["expansionChanges"]:
            parsed_expansion_changes.append(parse_pane_expansion_log(raw_expansion_change))
    if (raw_logs["paneContentChanges"]):
        parsed_pane_content_changes = []
        for raw_pane_content_change in raw_logs["paneContentChanges"]:
            parsed_pane_content_changes.append(parse_pane_content_change_log(raw_pane_content_change))
    return TestCaseLog(
        expansion_changes = parsed_expansion_changes if parsed_expansion_changes is not None else None,
        pane_content_changes = parsed_pane_content_changes if parsed_pane_content_changes is not None else None
    )

def parse_hint_pane_log(raw_logs: dict) -> HintPaneLog:
    if (raw_logs["expansionChanges"]):
        parsed_expansion_changes = []
        for raw_expansion_change in raw_logs["expansionChanges"]:
            parsed_expansion_changes.append(parse_pane_expansion_log(raw_expansion_change))
    if (raw_logs["paneContentChanges"]):
        parsed_pane_content_changes = []
        for raw_pane_content_change in raw_logs["paneContentChanges"]:
            parsed_pane_content_changes.append(parse_pane_content_change_log(raw_pane_content_change))
    return HintPaneLog(
        expansion_changes = parsed_expansion_changes if parsed_expansion_changes is not None else None,
        pane_content_changes = parsed_pane_content_changes if parsed_pane_content_changes is not None else None
    )

def parse_stage_log(raw_logs: dict) -> StageLog:
    #Check whether it's an exit log or not
    
    #If it's not an exit log, parse the stage log
    #Parse program logs, window focus events, test case logs, and hint pane logs
    parsed_program_logs = None
    if "programLogs" in raw_logs:
        parsed_program_logs = []
        for raw_program_log in raw_logs["programLogs"]:
            parsed_program_logs.append(parse_program_log(raw_program_log))
    
    parsed_window_focus_events = None
    if "focusEvents" in raw_logs:
        parsed_window_focus_events = []
        for raw_window_focus_event in raw_logs["focusEvents"]:
            parsed_window_focus_events.append(parse_window_focus_event(raw_window_focus_event))
    
    parsed_test_case_log = None
    if "testCaseLog" in raw_logs:
        parsed_test_case_log = parse_test_case_log(raw_logs["testCaseLog"])
    
    parsed_hint_pane_log = None
    if "hintPaneLogs" in raw_logs:
        parsed_hint_pane_log = parse_hint_pane_log(raw_logs["hintPaneLogs"])
    return StageLog(
        id = raw_logs["id"],
        time = raw_logs["time"],
        stage_string = raw_logs["stage"],
        program_logs = parsed_program_logs if parsed_program_logs is not None else None,
        response = raw_logs["response"] if "response" in raw_logs else None,
        correct = raw_logs["correct"] if "correct" in raw_logs else None,
        focus_events = parsed_window_focus_events if parsed_window_focus_events is not None else None,
        test_case_logs = parsed_test_case_log if parsed_test_case_log is not None else None,
        hint_pane_logs = parsed_hint_pane_log if parsed_hint_pane_log is not None else None
    )

def parse_student_id(raw_logs: dict) -> StudentId:
    return StudentId(
        id = raw_logs["id"],
        school = raw_logs["school"],
        date_first_accessed = raw_logs["dateFirstAccessed"] if "dateFirstAccessed" in raw_logs else None
    )