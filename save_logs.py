import json

"""
    These methods save unparsed logs to local .json files
    This is to avoid writing pointless .to_dict() functions in each class, as they're not needed for anything else
"""

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
