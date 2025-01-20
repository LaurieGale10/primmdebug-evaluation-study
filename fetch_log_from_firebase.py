import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import json

from classes.ExerciseLog import ExerciseLog
from classes.StageLog import StageLog
from classes.StudentId import StudentId
from parse_logs import *

global db

def get_firestore_client():
    cred = credentials.Certificate("firebase_service_account_key.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()

def load_exercise_logs_from_firebase(stage_logs: list[StageLog], mock_data: bool = False) -> list[ExerciseLog]:
    exercise_logs_ref = db.collection("exercise_logs") if not mock_data else db.collection("mock_exercise_logs")
    exercise_log_docs = exercise_logs_ref.stream()
    parsed_exercise_logs = []
    for doc in exercise_log_docs:
        doc_dict = doc.to_dict()
        doc_dict["id"] = doc.id
        stage_log_ids = doc_dict["stageLogIds"]
        stage_logs_for_exercise = [stage_log for stage_log in stage_logs if stage_log.id in stage_log_ids]
        parsed_exercise_logs.append(parse_exercise_log(doc_dict, stage_logs_for_exercise))
    return parsed_exercise_logs

def load_stage_logs_from_firebase(mock_data: bool = False) -> list[StageLog]:
    stage_logs_ref = db.collection("stage_logs") if not mock_data else db.collection("mock_stage_logs")
    stage_log_docs = stage_logs_ref.stream()

    parsed_stage_logs = []
    for doc in stage_log_docs:
        doc_dict = doc.to_dict()
        doc_dict["id"] = doc.id
        parsed_stage_logs.append(parse_stage_log(doc_dict))
    return parsed_stage_logs

def load_student_ids_from_firebase(mock_data: bool = False) -> list[StudentId]:
    student_ids_ref = db.collection("student_ids") if not mock_data else db.collection("mock_student_ids")
    student_id_docs = student_ids_ref.stream()

    parsed_student_ids = []
    for doc in student_id_docs:
        doc_dict = doc.to_dict()
        doc_dict["id"] = doc.id
        parsed_student_ids.append(parse_student_id(doc_dict))
    return parsed_student_ids

db = get_firestore_client()

stage_logs: list[StageLog] = load_stage_logs_from_firebase()
exercise_logs: list[ExerciseLog] = load_exercise_logs_from_firebase(stage_logs)
student_ids: list[StudentId] = load_student_ids_from_firebase()