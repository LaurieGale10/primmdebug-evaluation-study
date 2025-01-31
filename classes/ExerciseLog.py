import datetime

from classes.StageLog import StageLog
from classes.TimestampParser import TimestampParser


class ExerciseLog:
    def __init__(self, student_id: str, exercise_name: str, stage_logs: list[StageLog], start_time: str):
        self._student_id: str = student_id
        self._exercise_name: str = exercise_name
        self._stage_logs: list[StageLog] = stage_logs
        self._start_time: datetime = TimestampParser.parse_timestamp_str(start_time)
    
    @property
    def student_id(self) -> str:
        return self._student_id

    @property
    def exercise_name(self) -> str:
        return self._exercise_name

    @property
    def stage_logs(self) -> list[StageLog]:
        return self._stage_logs

    @property
    def start_time(self) -> str:
        return self._start_time
    
    @staticmethod
    def parse_exercise_log(raw_exercise_logs: dict, stage_logs: list[StageLog]) -> 'ExerciseLog':
        return ExerciseLog(
            student_id = raw_exercise_logs["studentId"],
            exercise_name = raw_exercise_logs["exerciseId"],
            stage_logs = stage_logs,
            start_time = raw_exercise_logs["time"]
        )
    
    def __repr__(self):
        return f'ExerciseLog(\'{self._student_id}\', \'{self._exercise_name}\', {self._start_time}, {self._stage_logs})'
