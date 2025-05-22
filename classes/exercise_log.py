import datetime

from classes.stage_log import StageLog
from classes.timestamp_parser import TimestampParser
from enums import DebuggingStage

class ExerciseLog:
    def __init__(self, student_id: str, exercise_name: str, stage_logs: list[StageLog], start_time: str, end_time: str, session: int):
        self._student_id: str = student_id
        self._exercise_name: str = exercise_name
        self._stage_logs: list[StageLog] = ExerciseLog.sort_stage_logs(stage_logs)
        self._start_time: datetime = TimestampParser.parse_timestamp_str(start_time)
        self._end_time: datetime = TimestampParser.parse_timestamp_str(end_time)
        self._session: int = session
    
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
    def start_time(self) -> datetime:
        return self._start_time
    
    @property
    def end_time(self) -> datetime:
        return self._end_time
    
    @property
    def session(self) -> int:
        return self._session
    
    @staticmethod
    def parse_exercise_log(raw_exercise_logs: dict, stage_logs: list[StageLog]) -> 'ExerciseLog':
        return ExerciseLog(
            student_id = raw_exercise_logs["studentId"],
            exercise_name = raw_exercise_logs["exerciseId"],
            stage_logs = stage_logs,
            start_time = raw_exercise_logs["startTime"],
            end_time = raw_exercise_logs["endTime"],
            session = raw_exercise_logs.get("session")
        )
    
    @staticmethod
    def sort_stage_logs(stage_logs: list[StageLog]) -> list[StageLog]:
        exit_logs: list[StageLog] = []
        non_exit_logs: list[StageLog] = []
        for log in stage_logs:
            if log.stage_name == DebuggingStage.exit:
                if exit_logs == []:
                    exit_logs.append(log)
            else:
                non_exit_logs.append(log)
        non_exit_logs.sort(key=lambda log: log.overall_stage_number)
        return non_exit_logs + exit_logs
    
    def __repr__(self):
        return f'ExerciseLog(\'{self._student_id}\', \'{self._exercise_name}\', {self._start_time}, {self._stage_logs})'
