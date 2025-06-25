import unittest
from testing_service.program_tests.nursery_rhyme_test import NurseryRhymeTest
from testing_service.test_report import TestReport

class TestNurseryRhymeTest(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(NurseryRhymeTest.run_tests("tests/testing_service/mock_programs/nursery_rhyme/correct_implementation.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 1)

    def test_original_program(self):
        test_report: TestReport = TestReport.parse_test_report(NurseryRhymeTest.run_tests("tests/testing_service/mock_programs/nursery_rhyme/original_implementation.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 1)

    def test_logically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(NurseryRhymeTest.run_tests("tests/testing_service/mock_programs/nursery_rhyme/logically_incorrect_implementation.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 1)

if __name__ == '__main__':
    unittest.main()