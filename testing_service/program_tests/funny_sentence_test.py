from ..test_case import TestCase
from ..exercise_test_runner import ExerciseTestRunner

class FunnySentenceTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["64","sneaky","elephant"],
            expected_output="Wow! I just saw 64 sneaky elephants juggling pineapples down the street!\n"
        ),
        TestCase(
            inputs=["1000","massive","tiger"],
            expected_output="Wow! I just saw 1000 massive tigers juggling pineapples down the street!\n"
        ),
        TestCase(
            inputs=["Zero","small","mouse"], #Need to work out how to check whether an error has been appropriately caught
            expected_output="ValueError: invalid literal for int() with base 10: 'Zero' on line 1\n"
        )
    ]

    @staticmethod
    def run_tests(program_filename: str) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, FunnySentenceTest.test_cases)