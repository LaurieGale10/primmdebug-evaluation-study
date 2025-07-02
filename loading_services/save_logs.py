import json
import csv

from classes.exercise_log import ExerciseLog
from classes.written_response import WrittenResponse
from classes.processors.exercise_log_processor import ExerciseLogProcessor
from enums import DebuggingStage
from loading_services.clean_logs import clean_exercise_and_stage_logs
from loading_services.fetch_log_from_firebase import *
from loading_services.fetch_logs_from_file import *

def save_exercises(exercises: list[dict], file_name: str = "exercises"):
    with open(f"data/{file_name}.json", "w") as f:
        f.write("[\n")
        f.write(",\n".join([json.dumps(doc, indent=4, default=str) for doc in exercises]))
        f.write("\n]")

def save_exercise_logs(exercise_logs: list[dict], file_name: str = "exercise_logs"):
    with open(f"data/{file_name}.json", "w") as f:
        f.write("[\n")
        f.write(",\n".join([json.dumps(doc, indent=4, default=str) for doc in exercise_logs]))
        f.write("\n]")

def save_stage_logs(stage_logs: list[dict], file_name: str = "stage_logs"):
    with open(f"data/{file_name}.json", "w") as f:
        f.write("[\n")
        f.write(",\n\t".join([json.dumps(doc, indent=4, default=str) for doc in stage_logs]))
        f.write("\n]")

def save_student_ids(student_ids: list[dict], file_name: str = "student_ids"):
    with open(f"data/{file_name}.json", "w") as f:
        f.write("[\n")
        f.write(",\n\t".join([json.dumps(doc, indent=4, default=str) for doc in student_ids]))
        f.write("\n]")

def get_written_response_data(exercise_log: ExerciseLog) -> list[WrittenResponse]: #TODO: Move to different save_logs.py as this doesn't concern data used directly for log data
    responses: list[WrittenResponse] = []
    for stage_log in exercise_log.stage_logs:
        if stage_log.stage_name in [DebuggingStage.predict, DebuggingStage.spot_defect, DebuggingStage.inspect_code, DebuggingStage.fix_error]:
            response_data: WrittenResponse = WrittenResponse(exercise_log.exercise_name, stage_log.stage_name, stage_log.end_time, stage_log.response)
            responses.append(response_data)
    return responses

def save_written_responses(exercise_logs: list[ExerciseLog], file_name: str = "written_responses"):
    with open(f"data/{file_name}.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["time", "exercise_id", "stage", "response"])
        written_responses: list[WrittenResponse] = [response for exercise_log in exercise_logs for response in get_written_response_data(exercise_log)]
        written_responses.sort(key=lambda r: (r.end_time.year, r.end_time.month, r.end_time.day, r.exercise_name, list(DebuggingStage).index(r.debugging_stage)))
        for response in written_responses:
            writer.writerow([response.end_time.strftime("%d/%m/%Y"), response.exercise_name, DebuggingStage(response.debugging_stage).value, response.response])

def save_all_logs():
    """
    Saves all the logs (exerise data, exercise attempts, stage logs, student ids) to local .json files, by loading and cleaning data from Firebase
    """
    raw_student_ids: list[dict] = load_student_ids_from_firebase()
    raw_stage_logs: list[dict] = load_stage_logs_from_firebase()
    raw_exercise_logs: list[dict] = load_exercise_logs_from_firebase()
    cleaned_exercise_logs, cleaned_stage_logs = clean_exercise_and_stage_logs(raw_exercise_logs, raw_stage_logs, raw_student_ids)

    save_student_ids(raw_student_ids)
    save_exercise_logs(cleaned_exercise_logs, "cleaned_exercise_logs")
    save_stage_logs(cleaned_stage_logs, "cleaned_stage_logs")

def save_clean_logs():
    """
    Saves all the logs (exerise data, exercise attempts, stage logs, student ids) to local .json files, by loading and cleaning data from Firebase
    """
    raw_student_ids: list[dict] = fetch_data_from_json("data/student_ids")
    raw_stage_logs: list[dict] = fetch_data_from_json("data/stage_logs")
    raw_exercise_logs: list[dict] = fetch_data_from_json("data/exercise_logs")
    cleaned_exercise_logs, cleaned_stage_logs = clean_exercise_and_stage_logs(raw_exercise_logs, raw_stage_logs, raw_student_ids)

    save_student_ids(raw_student_ids)
    save_exercise_logs(cleaned_exercise_logs)
    save_stage_logs(cleaned_stage_logs)