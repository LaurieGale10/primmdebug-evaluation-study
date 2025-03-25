import datetime

from enums import DebuggingStage

class WrittenResponse:

    def __init__(self, exercise_name: str, debugging_stage: DebuggingStage, end_time: datetime, response: str):
        self.exercise_name: str = exercise_name
        self.debugging_stage: DebuggingStage = debugging_stage
        self.end_time: datetime = end_time
        self.response: str = response
        
        @property
        def exercise_name(self) -> str:
            return self._exercise_name

        @property
        def debugging_stage(self) -> DebuggingStage:
            return self._debugging_stage

        @property
        def end_time(self) -> datetime:
            return self._end_time

        @property
        def response(self) -> str:
            return self._response