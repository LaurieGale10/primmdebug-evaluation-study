import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise_test_runner import ExerciseTestRunner
from test_case import TestCase

class TimesTableTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["0"],
            expected_output="The first 12 multiples of the number 0  are:\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n",
        ),
        TestCase(
            inputs=["5"],
            expected_output="The first 12 multiples of the number 5  are:\n5\n10\n15\n20\n25\n30\n35\n40\n45\n50\n55\n60\n",
        ),
        TestCase(
            inputs=["Zero"],
            exception_type=ValueError
        ),
    ]

    @staticmethod
    def run_tests(program_filename: str, normalise_output: bool = False) -> dict[str, int]:
        return ExerciseTestRunner.run_tests(program_filename, TimesTableTest.test_cases, normalise_output=normalise_output)

if __name__ == "__main__":
    filename: str = sys.argv[1]
    normalise_output: bool = bool(sys.argv[2]) if len(sys.argv) > 2 else False
    test_results: dict[str, int] = TimesTableTest.run_tests(filename, normalise_output=normalise_output)
    ExerciseTestRunner.save_test_results(test_results, filename)