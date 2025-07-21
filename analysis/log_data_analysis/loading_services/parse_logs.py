from analysis.log_data_analysis.classes.exercise_log import ExerciseLog
from analysis.log_data_analysis.classes.stage_log import StageLog
from analysis.log_data_analysis.classes.student_id import StudentId
from analysis.log_data_analysis.classes.exercise_classes.exercise import Exercise
from analysis.log_data_analysis.loading_services.clean_logs import *
from analysis.log_data_analysis.enums import DebuggingStage

def parse_exercises(raw_data: list[dict]) -> list[Exercise]:
    parsed_exercises = []
    for exercise in raw_data:
        parsed_exercises.append(Exercise.parse_exercise(exercise))
    return parsed_exercises

def parse_exercise_logs(stage_logs: list[StageLog], raw_logs: list[dict]) -> list[ExerciseLog]:
    parsed_exercise_logs = []
    for log in raw_logs:
        stage_log_ids = log["stageLogIds"]
        #Filter stage logs to only include those that are relevant to the exercise log
        stage_logs_for_exercise = [stage_log for stage_log in stage_logs if stage_log.id in stage_log_ids]
        parsed_exercise_logs.append(ExerciseLog.parse_exercise_log(log, stage_logs_for_exercise))
    return parsed_exercise_logs

def parse_stage_logs(raw_logs: list[dict]) -> list[StageLog]:
    parsed_stage_logs = []
    for log in raw_logs:
        parsed_stage_logs.append(StageLog.parse_stage_log(log))
    return parsed_stage_logs

def parse_student_ids(raw_logs: list[dict], exercise_logs: list[ExerciseLog]) -> list[StudentId]:
    parsed_student_ids = []
    for log in raw_logs:
        #Only parse student IDs for students who have attempted at least one exercise
        if any(exercise_log.student_id == log["id"] for exercise_log in exercise_logs):
            parsed_student_ids.append(StudentId.parse_student_id(log))
    return parsed_student_ids
