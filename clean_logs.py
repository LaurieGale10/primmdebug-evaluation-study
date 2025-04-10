from classes.ExerciseLog import ExerciseLog
from classes.StageLog import StageLog
from classes.WindowFocusEvent import WindowFocusEvent
from classes.TimestampParser import TimestampParser
from enums import DebuggingStage, FocusType
from loading_services.fetch_logs_from_file import fetch_data_from_json
from save_logs import *

import datetime

def format_start_end_times(exercise_log: ExerciseLog) -> ExerciseLog:
    """Reformats the stage and exercise logs such that they contain start and end times to them, making it easier to work out temporal-related data.

    Args:
        exercise_log (ExerciseLog): Exercise log object containing sorted exercise logs.
    """
    #If the first focus event (if existent) of the exercise log preces the start time of the exercise (known bug with logging), change the start time of the exercise
    if exercise_log.stage_logs[0].focus_events is not None and exercise_log.stage_logs[0].focus_events[0].time < exercise_log.start_time:
        setattr(exercise_log, '_start_time', exercise_log.stage_logs[0].focus_events[0].time)
    setattr(exercise_log.stage_logs[0], '_start_time', exercise_log.start_time)
    i: int = 1
    while (i < len(exercise_log.stage_logs)) and (exercise_log.stage_logs[i].stage_name != DebuggingStage.exit):
        setattr(exercise_log.stage_logs[i], '_start_time', exercise_log.stage_logs[i - 1].end_time)
        i += 1
    i = len(exercise_log.stage_logs) - 1 if i == len(exercise_log.stage_logs) else i #Reset value of i if too large
    if exercise_log.stage_logs[i].stage_name == DebuggingStage.exit:
        setattr(exercise_log, '_end_time', exercise_log.stage_logs[i].time)
    else:
        setattr(exercise_log, '_end_time', exercise_log.stage_logs[i].end_time)
    return exercise_log

def clean_focus_events(stage_log: StageLog) -> StageLog:
    """Take focus event of of a nature (i.e. focus_out or focus_in) and remove all succeeding focus events of the same value."""
    if stage_log.focus_events is not None:
        cleaned_focus_events: list[WindowFocusEvent] = []
        i: int = 1
        current_focus_value: FocusType = stage_log.focus_events[0].focus
        cleaned_focus_events.append(stage_log.focus_events[0])
        while (i < len(stage_log.focus_events)):
            if stage_log.focus_events[i].focus != current_focus_value:
                cleaned_focus_events.append(stage_log.focus_events[i])
                current_focus_value = stage_log.focus_events[i].focus
            i += 1
        stage_log.focus_events = cleaned_focus_events
    return stage_log

def add_session_data():
    raw_student_ids: list[dict] = fetch_data_from_json("data/student_ids")
    student_id_strings: list[str] = [student_id['id'] for student_id in raw_student_ids]
    raw_exercise_logs: list[dict] = fetch_data_from_json("data/exercise_logs")
    for student_id in student_id_strings:
        student_exercise_logs: list[dict] = [exercise_log for exercise_log in raw_exercise_logs if exercise_log['studentId'] == student_id]
        #Create sorted list of dates
        if len(student_exercise_logs) > 0:
            exercise_dates_per_student: list[str] = sorted(set(TimestampParser.parse_timestamp_str(exercise_log["time"]).strftime("%Y-%m-%d") for exercise_log in student_exercise_logs))
        #Add session number to each exercise log
        for log in student_exercise_logs:
            parsed_log_timestamp: str = TimestampParser.parse_timestamp_str(log["time"]).strftime("%Y-%m-%d")
            log["session"] = exercise_dates_per_student.index(parsed_log_timestamp) + 1
    #Save exercise logs to file
    save_exercise_logs(raw_exercise_logs, "exercise_logs_with_session_data")

add_session_data()