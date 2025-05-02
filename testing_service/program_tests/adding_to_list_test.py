from ..test_case import TestCase
from testing_service.exercise_test_runner import ExerciseTestRunner

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
    def run_tests(program_filename: str) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, AddingToListTest.test_cases)