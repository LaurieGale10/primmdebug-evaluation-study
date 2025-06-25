import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise_test_runner import ExerciseTestRunner
from test_case import TestCase

class CapitalOfHungaryTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["Budapest"],
            expected_output="You answered: Budapest\nCorrect!\n"
        ),
        TestCase(
            inputs=[""],
            expected_output="You answered: \nIncorrect. The correct answer is Budapest.\n"
        ),
        TestCase(
            inputs=["Paris"],
            expected_output="You answered: Paris\nIncorrect. The correct answer is Budapest.\n"
        ),
        TestCase(
            inputs=["   Budapest   "],
            expected_output="You answered:    Budapest   \nIncorrect. The correct answer is Budapest.\n"
        ),
    ]

    @staticmethod
    def run_tests(program_filename: str, normalise_output: bool = False) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, CapitalOfHungaryTest.test_cases, normalise_output=normalise_output)

if __name__ == "__main__":
    filename: str = sys.argv[1]
    normalise_output: bool = bool(sys.argv[2])
    test_results: dict[str, int] = CapitalOfHungaryTest.run_tests(filename, normalise_output=normalise_output)
    ExerciseTestRunner.save_test_results(test_results, filename)