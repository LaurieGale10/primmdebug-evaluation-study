import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise_test_runner import ExerciseTestRunner
from test_case import TestCase

class FunnySentenceTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["64","sneaky","elephant"],
            expected_output="Wow! I just saw 64 sneaky elephants juggling pineapples down the street!\n"
        ),
        TestCase(
            inputs=["1000","massive","tiger"],
            expected_output="Wow! I just saw 1000 massive tigers juggling pineapples down the street!\n"
        ),
        TestCase(
            inputs=["Zero","small","mouse"],
            exception_type=ValueError
        )
    ]

    @staticmethod
    def run_tests(program_filename: str, normalise_output: bool = False) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, FunnySentenceTest.test_cases, normalise_output=normalise_output)

if __name__ == "__main__":
    filename: str = sys.argv[1]
    normalise_output: bool = bool(sys.argv[2]) if len(sys.argv) > 2 else False
    test_results: dict[str, int] = FunnySentenceTest.run_tests(filename, normalise_output=normalise_output)
    ExerciseTestRunner.save_test_results(test_results, filename)