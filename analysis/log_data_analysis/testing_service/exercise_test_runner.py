import json
import sys
import os
import io
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from test_case import TestCase

class ExerciseTestRunner:
    
    @staticmethod
    def run_test_case(program_filename: str, test_case: TestCase, normalise_output: bool = False, debug: bool = False) -> bool:
        """Runs a a single test case on a student's program the test case passed or failed.

        Args:
            program_filename (str): The filename of the student's program to run the test case on.
            test_case (TestCase): The test case to run on the student's program. This should always contain an expected_output field but not an inputs field (this can be None or []).
        
        Returns:
            bool: Whether the test case passed or failed (the output must be exactly correct to pass).
        """
        with open(program_filename) as program: #Should this have an except or just keep running?
            with patch('builtins.input', side_effect=test_case.inputs), \
                 patch('sys.stdout', new_callable=io.StringIO) as mock_output, \
                 patch('random.choice', side_effect=test_case.random_values) if test_case.random_values is not None else patch('random.choice', side_effect=lambda x: x[0]):
                try:
                    exec(program.read())
                except Exception as e:
                    if test_case.exception_type is not None and isinstance(e, test_case.exception_type):
                        return True
                    return False

        try:
            if debug:
                print(test_case.inputs)
                print(test_case.expected_output)
                print(mock_output.getvalue())
                print(mock_output.getvalue() == test_case.expected_output)
            if normalise_output:
                assert "".join(mock_output.getvalue().strip().lower().split()) == "".join(test_case.expected_output.strip().lower().split())
            else:
                assert mock_output.getvalue() == test_case.expected_output
            return True
        except AssertionError:
            return False

    @staticmethod
    def run_tests(program_filename: str, test_cases: TestCase, normalise_output: bool = False, debug: bool = False) -> dict[str, int]:
        """Tests the correctness of a student's program (saved to a file) by running a set of test cases.

        Args:
            program_filename (str): The filename of the student's program to be tested.

        Returns:
            dict[str, int]: A dictionary containing the number of successful tests and the total number of tests run. Can be extended to include more data.
        """
        total_tests = 0
        successful_tests = 0
        for test_case in test_cases:
            if ExerciseTestRunner.run_test_case(program_filename, test_case, normalise_output=normalise_output, debug=debug):
                successful_tests += 1
            total_tests += 1
        return {
            "successful_tests": successful_tests,
            "total_tests": total_tests
        }
    
    @staticmethod
    def save_test_results(test_results: dict[str, int], filename: str):
        """Saves the test results to a JSON file.

        Args:
            test_results (dict[str, int]): The test results to save.
            filename (str): The filename to save the test results to.
        """
        #Define output file path within the Docker container
        output_file_name: str = os.path.basename(filename).replace(".py", ".out.json")
        output_file_path: str = os.path.join("/shared/test_results/", output_file_name)
        with open(output_file_path, "w") as f:
            json.dump(test_results, f, indent=2)