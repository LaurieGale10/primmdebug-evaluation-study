import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise_test_runner import ExerciseTestRunner
from test_case import TestCase

class LowerToUpperCaseCharacterConversionTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["a"],
            expected_output="The uppercase version of a is A\n"
        ),
        TestCase(
            inputs=["W"],
            expected_output="The uppercase version of W is You did not input a lowercase letter\n"
        ),
        TestCase(
            inputs=["w"],
            expected_output="The uppercase version of w is W\n"
        ),
        TestCase(
            inputs=["~"],
            expected_output="The uppercase version of ~ is You did not input a lowercase letter\n"
        )
    ]

    @staticmethod
    def run_tests(program_filename: str, normalise_output: bool = False) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, LowerToUpperCaseCharacterConversionTest.test_cases, normalise_output=normalise_output)
    
if __name__ == "__main__":
    filename: str = sys.argv[1]
    normalise_output: bool = bool(sys.argv[2]) if len(sys.argv) > 2 else False
    test_results: dict[str, int] = LowerToUpperCaseCharacterConversionTest.run_tests(filename, normalise_output=normalise_output)
    ExerciseTestRunner.save_test_results(test_results, filename)