import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise_test_runner import ExerciseTestRunner
from test_case import TestCase

class NurseryRhymeTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=[],
            expected_output="1\n2\n3\n4\n5\nOnce I caught a fish alive\n6\n7\n8\n9\n10\nThen I let it go again\n"
        )
    ]

    @staticmethod
    def run_tests(program_filename: str, normalise_output: bool = False) -> dict[str, int]:
        return ExerciseTestRunner.run_tests(program_filename, NurseryRhymeTest.test_cases, normalise_output=normalise_output)

if __name__ == "__main__":
    filename: str = sys.argv[1]
    normalise_output: bool = bool(sys.argv[2]) if len(sys.argv) > 2 else False
    test_results: dict[str, int] = NurseryRhymeTest.run_tests(filename, normalise_output=normalise_output)
    ExerciseTestRunner.save_test_results(test_results, filename)