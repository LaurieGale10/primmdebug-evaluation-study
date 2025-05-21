from ..test_case import TestCase
from ..exercise_test_runner import ExerciseTestRunner

class CapitalOfHungaryTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["Budapest"],
            expected_output="You answered: Budapest\nCorrect!\n"
        ),
        TestCase(
            inputs=[""],
            expected_output="You answered: \nIncorrect. The correct answer is Budapest.\n"
        ),
        TestCase(
            inputs=["Paris"],
            expected_output="You answered: Paris\nIncorrect. The correct answer is Budapest.\n"
        ),
        TestCase(
            inputs=["   Budapest   "],
            expected_output="You answered:    Budapest   \nIncorrect. The correct answer is Budapest.\n"
        ),
    ]

#TODO: Put this in a if __name__ == "__main__" block and save the test results
    @staticmethod
    def run_tests(program_filename: str) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, CapitalOfHungaryTest.test_cases)