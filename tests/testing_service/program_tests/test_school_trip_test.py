import unittest
from testing_service.program_tests.school_trip_test import SchoolTripTest
from testing_service.test_report import TestReport

class TestSchoolTripTest(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 6)
        self.assertEqual(test_report.n_total_tests, 6)

    def test_original_program(self):

        test_report: TestReport = TestReport.parse_test_report(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/original.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 6)

    def test_incorrect_symbol_program(self):
        test_report: TestReport = TestReport.parse_test_report(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/incorrect_symbol.py"))
        self.assertEqual(test_report.n_successful_tests, 2)
        self.assertEqual(test_report.n_total_tests, 6)

    def test_incorrect_output_program(self):
        test_report: TestReport = TestReport.parse_test_report(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/incorrect_output.py"))
        self.assertEqual(test_report.n_successful_tests, 2)
        self.assertEqual(test_report.n_total_tests, 6)

    def test_syntactically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/syntactically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 6)
        
    def test_hard_coded_program(self):
        test_report: TestReport = TestReport.parse_test_report(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/hard_coded.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 6)
