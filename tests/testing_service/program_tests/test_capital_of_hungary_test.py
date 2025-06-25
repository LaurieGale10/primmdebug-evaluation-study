import unittest
from testing_service.program_tests.capital_of_hungary_test import CapitalOfHungaryTest
from testing_service.test_report import TestReport

class TestCapitalOfHungaryTest(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_extended_program(self):
        test_report: TestReport = TestReport.parse_test_report(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/extended.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_logically_incorrect_extended_program(self):
        test_report: TestReport = TestReport.parse_test_report(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/logically_incorrect_extended.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_synactically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/syntactically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_empty_program(self):
        test_report: TestReport = TestReport.parse_test_report(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/empty.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 4)
        
    def test_without_if(self):
        test_report: TestReport = TestReport.parse_test_report(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/without_if.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 4)