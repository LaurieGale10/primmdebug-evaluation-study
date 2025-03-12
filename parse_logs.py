from classes.ExerciseLog import ExerciseLog
from classes.StageLog import StageLog
from classes.StudentId import StudentId
from clean_logs import format_start_end_times

def parse_exercise_logs(stage_logs: list[StageLog], raw_logs: list[dict]) -> list[ExerciseLog]:
    parsed_exercise_logs = []
    for log in raw_logs:
        stage_log_ids = log["stageLogIds"]
        stage_logs_for_exercise = [stage_log for stage_log in stage_logs if stage_log.id in stage_log_ids]
        #Exercise logs that contain no actual stage logs (either empty or only contain exit logs) are not counted as attempted exercises
        if len(stage_logs_for_exercise) > 0 and not all(stage_log.stage_name == "exit" for stage_log in stage_logs_for_exercise):
            parsed_exercise_logs.append(format_start_end_times(ExerciseLog.parse_exercise_log(log, stage_logs_for_exercise))) #Ideally should be done to data directly but not essential
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
