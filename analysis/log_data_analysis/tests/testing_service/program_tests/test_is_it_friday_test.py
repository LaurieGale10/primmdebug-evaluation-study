import unittest
from testing_service.program_tests.is_it_friday_test import IsItFridayTest
from testing_service.test_report import TestReport

class TestIsItFridayTest(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 3)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_original_program(self):
        test_report: TestReport = TestReport.parse_test_report(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/original.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_semantically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/semantically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_lowercased_friday_program(self):
        test_report: TestReport = TestReport.parse_test_report(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/lowercased_friday.py"))
        self.assertEqual(test_report.n_successful_tests, 2)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_missing_if_statement_program(self):
        test_report: TestReport = TestReport.parse_test_report(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/missing_if_statement.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_extended_program(self):
        test_report: TestReport = TestReport.parse_test_report(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/extended.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_missing_input(self):
        test_report: TestReport = TestReport.parse_test_report(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/missing_input.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 3)

if __name__ == '__main__':
    unittest.main()