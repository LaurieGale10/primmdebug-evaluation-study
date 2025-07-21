import unittest
from testing_service.program_tests.number_timeline_test import NumberTimelineTest
from testing_service.test_report import TestReport

class TestNumberTimelineTest(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 7)
        self.assertEqual(test_report.n_total_tests, 7)

    def test_original_program(self):
        test_report: TestReport = TestReport.parse_test_report(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/original.py"))
        self.assertEqual(test_report.n_successful_tests, 5)
        self.assertEqual(test_report.n_total_tests, 7)

    def test_syntactically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/syntactically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 7)

    def test_semantically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/semantically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 2)
        self.assertEqual(test_report.n_total_tests, 7)

    def test_logically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/logically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 7)

    def test_different_print_statement_program(self):
        test_report: TestReport = TestReport.parse_test_report(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/different_print_statement.py"))
        self.assertEqual(test_report.n_successful_tests, 2)
        self.assertEqual(test_report.n_total_tests, 7)

    def test_hard_coded_program(self):
        test_report: TestReport = TestReport.parse_test_report(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/hard_coded.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 7)