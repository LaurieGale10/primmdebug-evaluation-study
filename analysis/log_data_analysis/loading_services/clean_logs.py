from analysis.log_data_analysis.classes.exercise_log import ExerciseLog
from analysis.log_data_analysis.classes.stage_log import StageLog
from analysis.log_data_analysis.classes.window_focus_event import WindowFocusEvent
from analysis.log_data_analysis.classes.timestamp_parser import TimestampParser
from analysis.log_data_analysis.enums import DebuggingStage, FocusType
from analysis.log_data_analysis.loading_services.fetch_logs_from_file import fetch_data_from_json

def add_session_data(raw_exercise_logs: list[dict], raw_student_ids: list[dict]) -> list[dict]:
    """
    Adds session information to exercise log to allow for sequence analysis

    Args:
        raw_exercise_logs (list[dict]): The exercise logs to add session data to.
        raw_student_ids (list[dict]): The student ids required for adding session data.

    Returns:
        list[dict]: The exercise logs with session data added.
    """
    student_id_strings: list[str] = [student_id['id'] for student_id in raw_student_ids]

    for student_id in student_id_strings:
        student_exercise_logs: list[dict] = [exercise_log for exercise_log in raw_exercise_logs if exercise_log['studentId'] == student_id]
        if len(student_exercise_logs) > 0:
            #Create sorted list of dates
            exercise_dates_per_student: list[str] = sorted(set(TimestampParser.parse_timestamp_str(str(exercise_log["time"])).strftime("%Y-%m-%d") for exercise_log in student_exercise_logs))
        #Add session number to each exercise log
        for log in student_exercise_logs:
            parsed_log_timestamp: str = TimestampParser.parse_timestamp_str(str(log["time"])).strftime("%Y-%m-%d")
            log["session"] = exercise_dates_per_student.index(parsed_log_timestamp) + 1
    return raw_exercise_logs

def remove_empty_exercise_logs(raw_exercise_logs: list[dict], raw_stage_logs: list[dict]) -> list[dict]:
    """
    Removes empty exercise logs (containing no completed stage logs) from the list of exercise logs.

    Args:
        raw_exercise_logs (list[dict]): The exercise logs to remove empty logs from.

    Returns:
        list[dict]: The exercise logs with empty logs removed.
    """
    non_empty_logs: list[dict] = []
    for exercise_log in raw_exercise_logs:
        #Get list of ordered stage logs associated to a particular exercise log
        stage_logs_for_exercise: list[dict] = sorted([log for log in raw_stage_logs if log["id"] in exercise_log["stageLogIds"]], key=lambda x: x["time"])
        if len(exercise_log["stageLogIds"]) > 0 and not all(stage_log["stage"] == "exit" for stage_log in stage_logs_for_exercise): #TODO: Latter part of this if condition doesn't appear to be working
            non_empty_logs.append(exercise_log)
    return non_empty_logs

def format_start_end_times(raw_stage_logs: list[dict], raw_exercise_logs: list[dict]) -> tuple[list[dict], list[dict]]: #TODO: Make into a function that takes raw exercise/stage logs
    cleaned_stage_logs: list[dict] = []
    cleaned_exercise_logs: list[dict] = raw_exercise_logs
    for exercise_log in cleaned_exercise_logs:
        #Get list of ordered stage logs associated to a particular exercise log
        stage_logs_for_exercise: list[dict] = sorted([log for log in raw_stage_logs if log["id"] in exercise_log["stageLogIds"]], key=lambda x: x["time"])
        #If the first focus event (if existent) of the exercise log precedes the start time of the exercise (known bug with logging), change the start time of the exercise
        if "focusEvents" in stage_logs_for_exercise[0] and TimestampParser.parse_timestamp_str(str(stage_logs_for_exercise[0]["focusEvents"][0]["time"])) < TimestampParser.parse_timestamp_str(str(exercise_log["time"])):
            exercise_log["startTime"] = stage_logs_for_exercise[0]["focusEvents"][0]["time"] #Implemented to sort a bug with the timestamp markings of some of the focus events
        else:
            exercise_log["startTime"] = exercise_log.pop("time")
        i: int = 0
        
        #Replace "time" fields with more specific "startTime" and "endTime" fields
        while (i < len(stage_logs_for_exercise)) and (stage_logs_for_exercise[i]["stage"] != "exit"):
            stage_logs_for_exercise[i]["endTime"] = stage_logs_for_exercise[i].pop("time")
            stage_logs_for_exercise[i]["startTime"] = stage_logs_for_exercise[i-1]["endTime"] if i > 0 else exercise_log["startTime"]
            i += 1
        if stage_logs_for_exercise[-1]["stage"] == "exit":
            exercise_log["endTime"] = stage_logs_for_exercise[-1]["time"]
        else:
            exercise_log["endTime"] = stage_logs_for_exercise[-1]["endTime"]
        cleaned_stage_logs.extend(stage_logs_for_exercise)
    return (cleaned_exercise_logs, cleaned_stage_logs)

def clean_raw_focus_events(raw_stage_logs: list[dict]) -> list[dict]:
    """
    Take a given focus event and remove all succeeding focus events of the same value.
    This method was implemented to account for a glitch in the focus events data; multiple focus events of the same value were being logged in quick succession.
    
    Args:
        raw_stage_logs (list[dict], optional): Stage logs with glitchy focus events. Defaults to None.

    Returns:
        list[dict]: Stage logs with cleaned focus events.
    """
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

def clean_exercise_and_stage_logs(raw_exercise_logs: list[dict], raw_stage_logs: list[dict], raw_student_ids: list[dict]) -> tuple[list[dict], list[dict]]:
    """Cleans the exercise and stage logs, which includes:
    - Removing empty exercise logs (or any just containing exit logs)
    - Adding session data to exercise logs
    - Formatting start and end times of exercise and stage logs
    - Cleaning focus events in stage logs


    Args:
        raw_exercise_logs (list[dict], optional): The exercise logs to clean.
        raw_stage_logs (list[dict], optional): The stage logs to clean.
        raw_student_ids (list[dict], optional): The student_ids (don't need to be cleaned but required for adding session data).

    Raises:
        ValueError: If not all three arguments are provided.

    Returns:
        tuple[list[dict], list[dict]]: A tuple of the nature (cleaned_exercise_logs, cleaned_stage_logs).
    """
    if raw_exercise_logs is None or raw_stage_logs is None or raw_student_ids is None:
        raise ValueError("All three arguments ('raw_exercise_logs', 'raw_stage_logs', and 'raw_student_ids') must be provided for cleaning.")
    
    non_empty_exercise_logs_with_session_data: list[dict] = add_session_data(remove_empty_exercise_logs(raw_exercise_logs, raw_stage_logs), raw_student_ids)
    cleaned_focus_events_stage_logs: list[dict] = clean_raw_focus_events(raw_stage_logs)
    return format_start_end_times(cleaned_focus_events_stage_logs, non_empty_exercise_logs_with_session_data)