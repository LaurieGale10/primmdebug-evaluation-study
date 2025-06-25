import unittest
from testing_service.program_tests.adding_to_list_test import AddingToListTest
from testing_service.test_report import TestReport

class TestAddingToList(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 5)
        self.assertEqual(test_report.n_total_tests, 5)

        normalised_output_test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/correct.py", normalise_output=True))
        self.assertEqual(normalised_output_test_report.n_successful_tests, 5)
        self.assertEqual(normalised_output_test_report.n_total_tests, 5)
        
    def test_original_program(self):
        test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/original.py"))
        self.assertEqual(test_report.n_successful_tests, 2)
        self.assertEqual(test_report.n_total_tests, 5)

        normalised_output_test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/original.py", normalise_output=True))
        self.assertEqual(normalised_output_test_report.n_successful_tests, 2)
        self.assertEqual(normalised_output_test_report.n_total_tests, 5)

    def test_missing_output(self):
        test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/missing_output.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 5)

        normalised_output_test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/missing_output.py", normalise_output=True))
        self.assertEqual(normalised_output_test_report.n_successful_tests, 1)
        self.assertEqual(normalised_output_test_report.n_total_tests, 5)

    def test_syntactically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/syntactically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 5)

    def test_semantically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/semantically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 5)

    def test_missing_append(self):
        test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/missing_append.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 5)
        
        normalised_output_test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/missing_append.py", normalise_output=True))
        self.assertEqual(normalised_output_test_report.n_successful_tests, 1)
        self.assertEqual(normalised_output_test_report.n_total_tests, 5)

    def test_hard_coded(self):
        test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/hard_coded.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 5)

        normalised_output_test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/hard_coded.py", normalise_output=True))
        self.assertEqual(normalised_output_test_report.n_successful_tests, 4)
        self.assertEqual(normalised_output_test_report.n_total_tests, 5)

    def test_upper_case_output(self):
        test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/upper_case_output.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 5)

        normalised_output_test_report: TestReport = TestReport.parse_test_report(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/upper_case_output.py", normalise_output=True))
        self.assertEqual(normalised_output_test_report.n_successful_tests, 5)
        self.assertEqual(normalised_output_test_report.n_total_tests, 5)