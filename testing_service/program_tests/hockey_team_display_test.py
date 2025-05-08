from ..test_case import TestCase
from ..exercise_test_runner import ExerciseTestRunner

class HockeyTeamDisplayTest:
    test_cases: list[TestCase] = [
        TestCase(
            inputs=["Chile", "China"],
            expected_output="Team 1: Ch\nTeam 2: Ch\n"
        ),
        TestCase(
            inputs=["France", "South Africa"],
            expected_output="Team 1: Fra\nTeam 2: Sou\n"
        ),
        TestCase(
            inputs=["Cambodia", "Colombia"],
            expected_output="Team 1: Ca\nTeam 2: Co\n"
        ),
        TestCase(
            inputs=["0123456","0123"],
            expected_output="Team 1: 012\nTeam 2: 01\n"
        ),
        TestCase(
            inputs=["AB","ABCDEF"],
            expected_output="Team 1: AB\nTeam 2: ABC\n"
        ),
        TestCase(
            inputs=["A","B"],
            expected_output="Team 1: A\nTeam 2: B\n"
        )
    ]

    @staticmethod
    def run_tests(program_filename: str) -> tuple[int, int]:
        return ExerciseTestRunner.run_tests(program_filename, HockeyTeamDisplayTest.test_cases)