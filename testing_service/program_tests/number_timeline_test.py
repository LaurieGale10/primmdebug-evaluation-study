import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise_test_runner import ExerciseTestRunner
from test_case import TestCase

class NumberTimelineTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["0", "2"],
            expected_output="0 1 2 "
        ),
        TestCase(
            inputs=["100", "96"],
            expected_output="100 99 98 97 96 "
        ),
        TestCase(
            inputs=["0", "0"],
            expected_output="0 "
        ),
        TestCase(
            inputs=["-5", "-2"],
            expected_output="-5 -4 -3 -2 "
        ),
        TestCase(
            inputs=["-5", "-10"],
            expected_output="-5 -6 -7 -8 -9 -10 "
        ),
        TestCase(
            inputs=["10.0", "-5"],
            exception_type=ValueError
        ),
        TestCase(
            inputs=["Zero", "One"],
            exception_type=ValueError
        )
    ]

    @staticmethod
    def run_tests(program_filename: str) -> dict[str, int]:
        return ExerciseTestRunner.run_tests(program_filename, NumberTimelineTest.test_cases)

if __name__ == "__main__":
    filename: str = sys.argv[1]
    test_results: dict[str, int] = NumberTimelineTest.run_tests(filename)
    ExerciseTestRunner.save_test_results(test_results, filename)