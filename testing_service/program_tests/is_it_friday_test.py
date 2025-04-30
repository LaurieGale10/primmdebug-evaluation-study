from ..test_case import TestCase
from testing_service.exercise_test_runner import ExerciseTestRunner

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
    def run_tests(program_filename: str) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, IsItFridayTest.test_cases)