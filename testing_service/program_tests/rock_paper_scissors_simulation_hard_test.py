import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise_test_runner import ExerciseTestRunner
from test_case import TestCase

class RockPaperScissorsSimulationHardTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["1"],
            random_values=["Rock"],
            expected_output="Player 1 has chosen Rock\nPlayer 2 has chosen Rock\nThe winner is Neither\n"
        ),
        TestCase(
            inputs=["1"],
            random_values=["Scissors"],
            expected_output="Player 1 has chosen Rock\nPlayer 2 has chosen Scissors\nThe winner is Player 1\n"
        ),
        TestCase(
            inputs=["1"],
            random_values=["Paper"],
            expected_output="Player 1 has chosen Rock\nPlayer 2 has chosen Paper\nThe winner is Player 2\n"
        ),
        TestCase(
            inputs=["2"],
            random_values=["Rock"],
            expected_output="Player 1 has chosen Paper\nPlayer 2 has chosen Rock\nThe winner is Player 1\n"
        ),
        TestCase(
            inputs=["2"],
            random_values=["Scissors"],
            expected_output="Player 1 has chosen Paper\nPlayer 2 has chosen Scissors\nThe winner is Player 2\n"
        ),
        TestCase(
            inputs=["2"],
            random_values=["Paper"],
            expected_output="Player 1 has chosen Paper\nPlayer 2 has chosen Paper\nThe winner is Neither\n"
        ),
        TestCase(
            inputs=["3"],
            random_values=["Rock"],
            expected_output="Player 1 has chosen Scissors\nPlayer 2 has chosen Rock\nThe winner is Player 2\n"
        ),
        TestCase(
            inputs=["3"],
            random_values=["Scissors"],
            expected_output="Player 1 has chosen Scissors\nPlayer 2 has chosen Scissors\nThe winner is Neither\n"
        ),
        TestCase(
            inputs=["3"],
            random_values=["Paper"],
            expected_output="Player 1 has chosen Scissors\nPlayer 2 has chosen Paper\nThe winner is Player 1\n"
        ),
        TestCase(
            inputs=["[[[]]]"],
            exception_type=ValueError
        ),
        TestCase(
            inputs=["-1","1"],
            random_values=["Rock"],
            expected_output="Enter either 1, 2, or 3\nPlayer 1 has chosen Rock\nPlayer 2 has chosen Rock\nThe winner is Neither\n"
        )
    ]

    @staticmethod
    def run_tests(program_filename: str) -> dict[str, int]:
        return ExerciseTestRunner.run_tests(program_filename, RockPaperScissorsSimulationHardTest.test_cases)

if __name__ == "__main__":
    filename: str = sys.argv[1]
    test_results: dict[str, int] = RockPaperScissorsSimulationHardTest.run_tests(filename)
    ExerciseTestRunner.save_test_results(test_results, filename)