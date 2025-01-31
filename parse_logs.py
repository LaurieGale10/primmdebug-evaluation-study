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


def parse_exercise_logs(stage_logs: list[StageLog], raw_logs: list[dict]) -> list[ExerciseLog]:
    parsed_exercise_logs = []
    for log in raw_logs:
        stage_log_ids = log["stageLogIds"]
        stage_logs_for_exercise = [stage_log for stage_log in stage_logs if stage_log.id in stage_log_ids]
        parsed_exercise_logs.append(ExerciseLog.parse_exercise_log(log, stage_logs_for_exercise))
    return parsed_exercise_logs

def parse_stage_logs(raw_logs: list[dict]) -> list[StageLog]:
    parsed_stage_logs = []
    for log in raw_logs:
        parsed_stage_logs.append(StageLog.parse_stage_log(log))
    return parsed_stage_logs

def parse_student_ids(raw_logs: list[dict]) -> list[StudentId]:
    parsed_student_ids = []
    for log in raw_logs:
        parsed_student_ids.append(StudentId.parse_student_id(log))
    return parsed_student_ids
