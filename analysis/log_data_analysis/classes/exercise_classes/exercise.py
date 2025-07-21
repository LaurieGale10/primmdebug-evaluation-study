from analysis.log_data_analysis.classes.exercise_classes.test_case import TestCase
from analysis.log_data_analysis.enums import DebuggingStage

class Exercise:
    def __init__(self, id: str, description: str, difficulty: str, program: str, line_containing_error: str = None, hints: dict[DebuggingStage, list[str]] = None, test_cases: list[TestCase] = None):
        self._name: str = id
        self._description: str = description
        if line_containing_error is not None:
            self._line_containing_error: int = int(line_containing_error)
        self._program: str = program
        self._hints: dict[DebuggingStage, list[str]] = hints
        self._test_cases: list[TestCase] = test_cases
        self._difficulty: str = difficulty

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description
    
    @property
    def difficulty(self) -> str:
        return self._difficulty
    
    @property
    def program(self) -> str:
        return self._program

    @property
    def line_containing_error(self) -> int:
        return self._line_containing_error if self._line_containing_error is not None else None

    @property
    def hints(self) -> dict[DebuggingStage, list[str]]:
        return self._hints if self._hints is not None else None

    @property
    def test_cases(self) -> list[TestCase]:
        return self._test_cases if self._test_cases is not None else None

    @staticmethod
    def parse_exercise(raw_data: dict) -> 'Exercise':
        parsed_test_cases = None
        if "test_cases" in raw_data:
            parsed_test_cases = []
            for raw_test_case in raw_data["test_cases"]:
                parsed_test_cases.append(TestCase.parse_test_case(raw_test_case))
        return Exercise(
            id = raw_data["id"],
            description = raw_data["description"],
            difficulty = raw_data["difficulty"],
            program = raw_data["program"],
            line_containing_error = raw_data.get("line_containing_error"),
            hints = raw_data.get("hints"),
            test_cases = parsed_test_cases
        )
