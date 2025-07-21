import unittest
from testing_service.program_tests.lower_to_upper_case_character_conversion_test import LowerToUpperCaseCharacterConversionTest
from testing_service.test_report import TestReport

class TestLowerToUpperCaseCharacterConversionTest(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_original_program(self):
        test_report: TestReport = TestReport.parse_test_report(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/original.py"))
        self.assertEqual(test_report.n_successful_tests, 2)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_no_return_program(self):
        test_report: TestReport = TestReport.parse_test_report(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/no_return.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_incorrect_inequalities_program(self):
        test_report: TestReport = TestReport.parse_test_report(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/incorrect_inequalities.py"))
        self.assertEqual(test_report.n_successful_tests, 3)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_anded_condition_program(self):
        test_report: TestReport = TestReport.parse_test_report(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/anded_conditon.py"))
        self.assertEqual(test_report.n_successful_tests, 2)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_syntactically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/syntactically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_semantically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/semantically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 2)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_printf_statement_program(self):
        test_report: TestReport = TestReport.parse_test_report(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/printf_statement.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 4)

    def test_hard_coded_program(self):
        test_report: TestReport = TestReport.parse_test_report(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/hard_coded.py"))
        self.assertEqual(test_report.n_successful_tests, 3)
        self.assertEqual(test_report.n_total_tests, 4)