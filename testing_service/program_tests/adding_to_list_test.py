import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise_test_runner import ExerciseTestRunner
from test_case import TestCase

class AddingToListTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["100"],
            expected_output="Initial list: [5, 7, 12]\nUpdated list: [5, 7, 12, 100]\n"   
        ),
        TestCase(
            inputs=["1"],
            expected_output="Initial list: [5, 7, 12]\nUpdated list: [1, 5, 7, 12]\n"
        ),
        TestCase(
           inputs=["6"],
           expected_output="Initial list: [5, 7, 12]\nUpdated list: [5, 6, 7, 12]\n"
        ),
        TestCase(
            inputs=["-1"],
            expected_output="Initial list: [5, 7, 12]\nUpdated list: [-1, 5, 7, 12]\n"
        ),

        TestCase(
            inputs=["Zero"],
            exception_type=ValueError,
        )
    ]

    @staticmethod
    def run_tests(program_filename: str) -> dict[str, int]:
        return ExerciseTestRunner.run_tests(program_filename, AddingToListTest.test_cases)

if __name__ == "__main__":
    filename: str = sys.argv[1]
    test_results: dict[str, int] = AddingToListTest.run_tests(filename)
    ExerciseTestRunner.save_test_results(test_results, filename)