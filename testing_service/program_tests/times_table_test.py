from testing_service.test_case import TestCase
from testing_service.exercise_test_runner import ExerciseTestRunner

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
    def run_tests(program_filename: str) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, TimesTableTest.test_cases)