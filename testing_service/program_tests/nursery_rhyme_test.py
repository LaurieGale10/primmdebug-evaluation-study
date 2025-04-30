from testing_service.test_case import TestCase
from testing_service.exercise_test_runner import ExerciseTestRunner

class NurseryRhymeTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=[], #Not sure whether this should be none
            expected_output="1\n2\n3\n4\n5\nOnce I caught a fish alive\n6\n7\n8\n9\n10\nThen I let it go again\n"
        )
    ]

    @staticmethod
    def run_tests(program_filename: str) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, NurseryRhymeTest.test_cases)