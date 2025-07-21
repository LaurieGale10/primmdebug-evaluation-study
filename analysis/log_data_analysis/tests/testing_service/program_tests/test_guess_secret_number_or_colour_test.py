import unittest
from testing_service.program_tests.guess_secret_number_or_colour_test import GuessSecretNumberOrColourTest
from testing_service.test_report import TestReport

class TestGuessSecretNumberOrColourTest(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 6)
        self.assertEqual(test_report.n_total_tests, 6)
    
    def test_original_program(self):
        test_report: TestReport = TestReport.parse_test_report(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/original.py"))
        self.assertEqual(test_report.n_successful_tests, 5)
        self.assertEqual(test_report.n_total_tests, 6)
    
    def test_syntactically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/syntactically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 6)
    
    def test_missing_final_output_program(self):
        test_report: TestReport = TestReport.parse_test_report(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/missing_final_output.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 6)
    
    def test_incorrect_inequality_program(self):
        test_report: TestReport = TestReport.parse_test_report(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/incorrect_inequality.py"))
        self.assertEqual(test_report.n_successful_tests, 3)
        self.assertEqual(test_report.n_total_tests, 6)
    
    def test_semantically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/semantically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 6)
    
    def test_incorrect_assignments_program(self):
        test_report: TestReport = TestReport.parse_test_report(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/incorrect_assignments.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 6)