from ..test_case import TestCase
from ..exercise_test_runner import ExerciseTestRunner

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
    def run_tests(program_filename: str) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, RockPaperScissorsSimulationHardTest.test_cases, debug=True)