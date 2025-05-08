from ..test_case import TestCase
from ..exercise_test_runner import ExerciseTestRunner

class GuessSecretNumberOrColourTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["B", "42"],
            expected_output="Correct! The secret number is 42.\nProgram finished!\n",
        ),
        TestCase(
            inputs=["B", "1142", "42"],
            expected_output="Incorrect! Try again.\nCorrect! The secret number is 42.\nProgram finished!\n"
        ),
        TestCase(
            inputs=["B", "£*()", "-42", "42"],
            expected_output="Please enter a valid number.\nIncorrect! Try again.\nCorrect! The secret number is 42.\nProgram finished!\n",
        ),
        TestCase(
            inputs=["A", "blue"],
            expected_output="Correct! The secret colour is blue.\nProgram finished!\n",
        ),
        TestCase(
            inputs=["A", "red", "blue"],
            expected_output="Incorrect! Try again.\nCorrect! The secret colour is blue.\nProgram finished!\n",
        ),
        TestCase(
            inputs=["----"],
            expected_output="Invalid choice. Please restart the program and enter 'A' or 'B'.\nProgram finished!\n",
        )
    ]

    @staticmethod
    def run_tests(program_filename: str) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, GuessSecretNumberOrColourTest.test_cases)