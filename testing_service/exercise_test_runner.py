from testing_service.test_case import TestCase

import io
from unittest.mock import patch

class ExerciseTestRunner:
    
    @staticmethod
    def run_test_case(program_filename: str, test_case: TestCase) -> bool:
        """Runs a a single test case on a student's program the test case passed or failed.

        Args:
            program_filename (str): The filename of the student's program to run the test case on.
            test_case (TestCase): The test case to run on the student's program. This should always contain an expected_output field but not an inputs field (this can be None or []).
        
        Returns:
            bool: Whether the test case passed or failed (the output must be exactly correct to pass).
        """
        with open(f"{program_filename}.py") as program: #Should this have an except or just keep running?
            with patch('builtins.input', side_effect=test_case.inputs), patch('sys.stdout', new_callable=io.StringIO) as mock_output:
                try:
                    exec(program.read())  # Might not work when running in non-relative directory, so might have to switch back to importing
                except Exception as e:
                    if test_case.exception_type is not None and isinstance(e, test_case.exception_type):
                        return True
                    return False

        try:
            assert mock_output.getvalue() == test_case.expected_output
            return True
        except AssertionError:
            return False

    @staticmethod
    def run_tests(program_filename: str, test_cases: TestCase) -> tuple[int, int]:
        """Tests the correctness of a student's program (saved to a file) by running a set of test cases.

        Args:
            program_filename (str): The filename of the student's program to be tested.

        Returns:
            tuple[int, int]: A tuple containing the number of successful tests and the total number of tests run.
        """
        completed_tests = 0
        successful_tests = 0
        for test_case in test_cases:
            if ExerciseTestRunner.run_test_case(program_filename, test_case):
                successful_tests += 1
            completed_tests += 1
        return successful_tests, completed_tests