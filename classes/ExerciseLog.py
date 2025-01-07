from classes.StageLog import StageLog


class ExerciseLog:
    def __init__(self, student_id: str, exercise_name: str, stage_logs: list[StageLog], start_time):
        self._student_id = student_id
        self._exercise_name = exercise_name
        self._stage_logs = stage_logs
        self._start_time = start_time
    
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
    def start_time(self):
        return self._start_time
