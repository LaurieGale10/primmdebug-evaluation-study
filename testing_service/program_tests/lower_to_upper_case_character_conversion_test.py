from ..test_case import TestCase
from testing_service.exercise_test_runner import ExerciseTestRunner

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
    def run_tests(program_filename: str) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, LowerToUpperCaseCharacterConversionTest.test_cases)