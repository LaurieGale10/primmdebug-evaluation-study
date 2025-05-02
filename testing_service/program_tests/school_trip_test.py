from ..test_case import TestCase
from ..exercise_test_runner import ExerciseTestRunner

class SchoolTripTest:

    test_cases: list[TestCase] = [
        TestCase(
            inputs=["0"],
            expected_output="Number of full coaches needed: 0\nNumber of people on the partly full coach: 0\n"
        ),
        TestCase(
            inputs=["Zero"],
            exception_type=ValueError
        ),
        TestCase(
            inputs=["10.0"],
            exception_type=ValueError
        ),
        TestCase(
            inputs=["1"],
            expected_output="Number of full coaches needed: 0\nNumber of people on the partly full coach: 1\n"
        ),
        TestCase(
            inputs=["45"],
            expected_output="Number of full coaches needed: 1\nNumber of people on the partly full coach: 0\n"
        ),
        TestCase(
            inputs=["100"],
            expected_output="Number of full coaches needed: 2\nNumber of people on the partly full coach: 10\n"
        )
    ]

    @staticmethod
    def run_tests(program_filename: str) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, SchoolTripTest.test_cases)