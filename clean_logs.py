from classes.exercise_log import ExerciseLog
from classes.stage_log import StageLog
from classes.window_focus_event import WindowFocusEvent
from classes.timestamp_parser import TimestampParser
from enums import DebuggingStage, FocusType
from loading_services.fetch_logs_from_file import fetch_data_from_json
#from save_logs import *

def format_start_end_times(exercise_log: ExerciseLog) -> ExerciseLog: #TODO: Make into a function that takes raw exercise/stage logs
    """Reformats the stage and exercise logs such that they contain start and end times to them, making it easier to work out temporal-related data.

    Args:
        exercise_log (ExerciseLog): Exercise log object containing sorted exercise logs.
    """
    #If the first focus event (if existent) of the exercise log precedes the start time of the exercise (known bug with logging), change the start time of the exercise
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


def add_session_data(raw_exercise_logs: list[dict], raw_student_ids: list[dict]) -> list[dict]:
    """
    Adds session information to exercise log to allow for sequence analysis

    Args:
        raw_exercise_logs (list[dict]): The exercise logs to add session data to.
        raw_student_ids (list[dict]): _description_

    Returns:
        list[dict]: The exercise logs with session data added.
    """
    raw_student_ids: list[dict] = fetch_data_from_json("data/student_ids")
    student_id_strings: list[str] = [student_id['id'] for student_id in raw_student_ids]
    raw_exercise_logs: list[dict] = fetch_data_from_json("data/exercise_logs")
    for student_id in student_id_strings:
        student_exercise_logs: list[dict] = [exercise_log for exercise_log in raw_exercise_logs if exercise_log['studentId'] == student_id]
        if len(student_exercise_logs) > 0:
            #Create sorted list of dates
            exercise_dates_per_student: list[str] = sorted(set(TimestampParser.parse_timestamp_str(exercise_log["time"]).strftime("%Y-%m-%d") for exercise_log in student_exercise_logs))
        #Add session number to each exercise log
        for log in student_exercise_logs:
            parsed_log_timestamp: str = TimestampParser.parse_timestamp_str(log["time"]).strftime("%Y-%m-%d")
            log["session"] = exercise_dates_per_student.index(parsed_log_timestamp) + 1
    #save_exercise_logs(raw_exercise_logs, "exercise_logs_with_session_data")
    return raw_exercise_logs

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

def clean_raw_focus_events(raw_stage_logs: list[dict] = None) -> list[dict]: ##TODO: Refactored this to clean raw focus events; do the same with format_start_end_times and then get rid of the other functions and create a pipeline for cleaning data before parsing it
    """
    Take focus event of of a nature (i.e. focus_out or focus_in) and remove all succeeding focus events of the same value.
    
    Args:
        raw_stage_logs (list[dict], optional): _description_. Defaults to None.

    Returns:
        list[dict]: _description_
    """
    raw_stage_logs: list[dict] = fetch_data_from_json("data/stage_logs")
    for log in raw_stage_logs:
        if "focusEvents" in log:
            distinct_focus_events: list[dict] = []
            raw_focus_events: list[dict] = log["focusEvents"]
            i: int = 1
            current_focus_value: str = raw_focus_events[0]["focus"]
            distinct_focus_events.append(raw_focus_events[0])
            while (i < len(raw_focus_events)):
                if raw_focus_events[i]["focus"] != current_focus_value:
                    distinct_focus_events.append(raw_focus_events[i])
                    current_focus_value = raw_focus_events[i]["focus"]
                i += 1
            log["focusEvents"] = distinct_focus_events
    #save_exercise_logs(raw_stage_logs, "stage_logs_with_cleaned_focus_events")
    return raw_stage_logs

def clean_exercise_logs(raw_exercise_logs: list[dict], raw_student_ids: list[dict]) -> list[dict]:
    if raw_exercise_logs is None or raw_student_ids is None:
        raise ValueError("Both 'raw_exercise_logs' and 'raw_student_ids' must be provided for exercise log cleaning.")
    # Format start and end times and add session data
    return add_session_data(raw_exercise_logs, raw_student_ids)

def clean_stage_logs(raw_stage_logs: list[dict]) -> list[dict]:
    return clean_raw_focus_events(raw_stage_logs)