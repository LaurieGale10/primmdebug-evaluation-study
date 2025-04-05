import json
import csv

from classes.ExerciseLog import ExerciseLog
from classes.WrittenResponse import WrittenResponse
from classes.processors.ExerciseLogProcessor import ExerciseLogProcessor
from enums import DebuggingStage

"""
    These methods save unparsed logs to local .json files
    This is to avoid writing pointless .to_dict() functions in each class, as they're not needed for anything else
"""

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
    with open(f"data/{file_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["time", "exercise_id", "stage", "response"])
        written_responses: list[WrittenResponse] = [response for exercise_log in exercise_logs for response in get_written_response_data(exercise_log)]
        written_responses.sort(key=lambda r: (r.end_time.year, r.end_time.month, r.end_time.day, r.exercise_name, list(DebuggingStage).index(r.debugging_stage)))
        for response in written_responses:
            writer.writerow([response.end_time.strftime("%d/%m/%Y"), response.exercise_name, DebuggingStage(response.debugging_stage).value, response.response])