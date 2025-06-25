import unittest
from testing_service.program_tests.funny_sentence_test import FunnySentenceTest
from testing_service.test_report import TestReport

class TestFunnySentenceTest(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 3)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_orginal_program(self):
        test_report: TestReport = TestReport.parse_test_report(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/original.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_empty_program(self):
        test_report: TestReport = TestReport.parse_test_report(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/empty.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_correct_with_concatenation_program(self):
        test_report: TestReport = TestReport.parse_test_report(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/correct_with_concatenation.py"))
        self.assertEqual(test_report.n_successful_tests, 3)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_incorrect_output_program(self):
        test_report: TestReport = TestReport.parse_test_report(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/incorrect_output.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 3)

    def test_hard_coded_program(self):
        test_report: TestReport = TestReport.parse_test_report(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/hard_coded.py"))
        self.assertEqual(test_report.n_successful_tests, 2)
        self.assertEqual(test_report.n_total_tests, 3)