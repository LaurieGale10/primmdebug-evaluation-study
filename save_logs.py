import json
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.stream_generator import StreamGenerator

"""
    These methods save unparsed logs to local .json files
    This is to avoid writing pointless .to_dict() functions in each class, as they're not needed for anything else
"""

def save_exercise_logs(exercise_logs: StreamGenerator[DocumentSnapshot], file_name: str = "exercise_logs"):
    with open(f"data/{file_name}.json", "w") as f:
        f.write("[\n")
        f.write(",\n".join([json.dumps(doc.to_dict(), indent=4, default=str) for doc in exercise_logs]))
        f.write("\n]")

def save_stage_logs(stage_logs: StreamGenerator[DocumentSnapshot], file_name: str = "stage_logs"):
    with open(f"data/{file_name}.json", "w") as f:
        f.write("[\n")
        f.write(",\n\t".join([json.dumps(doc.to_dict(), indent=4, default=str) for doc in stage_logs]))
        f.write("\n]")

def save_student_ids(student_ids: StreamGenerator[DocumentSnapshot], file_name: str = "student_ids"):
    with open(f"data/{file_name}.json", "w") as f:
        f.write("[\n")
        f.write(",\n\t".join([json.dumps(doc.to_dict(), indent=4, default=str) for doc in student_ids]))
        f.write("\n]")
