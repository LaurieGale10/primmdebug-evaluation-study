import unittest
from testing_service.program_tests.times_table_test import TimesTableTest
from testing_service.test_report import TestReport

class TestTimesTableTest(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(TimesTableTest.run_tests("tests/testing_service/mock_programs/times_table/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 3)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_original_program(self):
        test_report: TestReport = TestReport.parse_test_report(TimesTableTest.run_tests("tests/testing_service/mock_programs/times_table/original.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_syntactically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(TimesTableTest.run_tests("tests/testing_service/mock_programs/times_table/semantically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_correct_printf_formatting(self):
        test_report: TestReport = TestReport.parse_test_report(TimesTableTest.run_tests("tests/testing_service/mock_programs/times_table/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 3)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_times_table_hard_coded(self):
        test_report: TestReport = TestReport.parse_test_report(TimesTableTest.run_tests("tests/testing_service/mock_programs/times_table/hard_coded.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 3)