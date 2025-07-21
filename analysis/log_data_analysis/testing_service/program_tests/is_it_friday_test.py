import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise_test_runner import ExerciseTestRunner
from test_case import TestCase

class IsItFridayTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["Friday"], #This is a correct test case as per the program description
            expected_output="Yay! It's Friday!\n"
        ),
        TestCase(
            inputs=["Monday"],
            expected_output=""
        ),
        TestCase( #Should this test case be an empty string or "Yay! It's Friday!"? More able students would improve the program, which I don't really want ti
            inputs=["friday"],
            expected_output=""
        )
    ]

    @staticmethod
    def run_tests(program_filename: str, normalise_output: bool = False) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, IsItFridayTest.test_cases, normalise_output=normalise_output)
    
if __name__ == "__main__":
    filename: str = sys.argv[1]
    normalise_output: bool = bool(sys.argv[2]) if len(sys.argv) > 2 else False
    test_results: dict[str, int] = IsItFridayTest.run_tests(filename, normalise_output=normalise_output)
    ExerciseTestRunner.save_test_results(test_results, filename)