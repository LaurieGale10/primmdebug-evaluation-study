from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.stream_generator import StreamGenerator

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


def parse_stage_log(raw_logs: dict) -> StageLog:
    #Check whether it's an exit log or not
    
    #If it's not an exit log, parse the stage log
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
    if "testCaseLog" in raw_logs:
        parsed_test_case_log = TestCaseLog.parse_test_case_log(raw_logs["testCaseLog"])
    
    parsed_hint_pane_log = None
    if "hintPaneLogs" in raw_logs:
        parsed_hint_pane_log = HintPaneLog.parse_hint_pane_log(raw_logs["hintPaneLogs"])
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

def parse_exercise_logs(stage_logs: list[StageLog], raw_logs: StreamGenerator[DocumentSnapshot]) -> list[ExerciseLog]:
    parsed_exercise_logs = []
    for doc in raw_logs:
        doc_dict = doc.to_dict()
        doc_dict["id"] = doc.id
        stage_log_ids = doc_dict["stageLogIds"]
        stage_logs_for_exercise = [stage_log for stage_log in stage_logs if stage_log.id in stage_log_ids]
        parsed_exercise_logs.append(ExerciseLog.parse_exercise_log(doc_dict, stage_logs_for_exercise))
    return parsed_exercise_logs

def parse_stage_logs(raw_logs: StreamGenerator[DocumentSnapshot]) -> list[StageLog]:
    parsed_stage_logs = []
    for doc in raw_logs:
        doc_dict = doc.to_dict()
        doc_dict["id"] = doc.id
        parsed_stage_logs.append(parse_stage_log(doc_dict))
    return parsed_stage_logs

def parse_student_ids(raw_logs: StreamGenerator[DocumentSnapshot]) -> list[StudentId]:
    parsed_student_ids = []
    for doc in raw_logs:
        doc_dict = doc.to_dict()
        doc_dict["id"] = doc.id
        parsed_student_ids.append(parse_student_id(doc_dict))
    return parsed_student_ids