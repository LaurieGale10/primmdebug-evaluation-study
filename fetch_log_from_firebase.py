import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

from parse_logs import *

global db

def get_firestore_client():
    cred = credentials.Certificate("firebase_service_account_key.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()

def load_exercise_logs_from_firebase(mock_data: bool = False) -> list[dict]:
    exercise_log_docs = db.collection("exercise_logs").stream() if not mock_data else db.collection("mock_exercise_logs").stream()
    raw_exercise_logs = []
    for doc in exercise_log_docs:
        doc_dict = doc.to_dict()
        doc_dict["id"] = doc.id
        raw_exercise_logs.append(doc_dict)
    return raw_exercise_logs

def load_stage_logs_from_firebase(mock_data: bool = False) -> list[dict]:
    stage_logs_docs = db.collection("stage_logs").stream() if not mock_data else db.collection("mock_stage_logs").stream()
    raw_stage_logs = []
    for doc in stage_logs_docs:
        doc_dict = doc.to_dict()
        doc_dict["id"] = doc.id
        raw_stage_logs.append(doc_dict)
    return raw_stage_logs

def load_student_ids_from_firebase(mock_data: bool = False) -> list[dict]:
    student_ids_docs = db.collection("student_ids").stream() if not mock_data else db.collection("mock_student_ids").stream()
    raw_student_ids = []
    for doc in student_ids_docs:
        doc_dict = doc.to_dict()
        doc_dict["id"] = doc.id
        raw_student_ids.append(doc_dict)
    return raw_student_ids

db = get_firestore_client()