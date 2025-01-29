import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.stream_generator import StreamGenerator

from parse_logs import *

global db

def get_firestore_client():
    cred = credentials.Certificate("firebase_service_account_key.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()

def load_exercise_logs_from_firebase(mock_data: bool = False) -> StreamGenerator[DocumentSnapshot]:
    exercise_logs_ref = db.collection("exercise_logs") if not mock_data else db.collection("mock_exercise_logs")
    return exercise_logs_ref.stream()

def load_stage_logs_from_firebase(mock_data: bool = False) -> StreamGenerator[DocumentSnapshot]:
    stage_logs_ref = db.collection("stage_logs") if not mock_data else db.collection("mock_stage_logs")
    return stage_logs_ref.stream()

def load_student_ids_from_firebase(mock_data: bool = False) -> StreamGenerator[DocumentSnapshot]:
    student_ids_ref = db.collection("student_ids") if not mock_data else db.collection("mock_student_ids")
    return student_ids_ref.stream()

db = get_firestore_client()