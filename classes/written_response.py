import datetime

from enums import DebuggingStage

class WrittenResponse:

    def __init__(self, exercise_name: str = None, exercise_description: str = None, debugging_stage: DebuggingStage = None, end_time: datetime = None, response: str = None):
        self._exercise_name: str = exercise_name
        self._exercise_description: str = exercise_description
        self._debugging_stage: DebuggingStage = debugging_stage
        self._end_time: datetime = end_time
        self._response: str = response

    @property
    def exercise_name(self) -> str:
        return self._exercise_name

    @property
    def exercise_description(self) -> str:
        return self._exercise_description

    @property
    def debugging_stage(self) -> DebuggingStage:
        return self._debugging_stage

    @property
    def end_time(self) -> datetime:
        return self._end_time

    @property
    def response(self) -> str:
        return self._response