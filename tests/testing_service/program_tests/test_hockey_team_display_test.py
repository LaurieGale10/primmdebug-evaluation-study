import unittest
from testing_service.program_tests.hockey_team_display_test import HockeyTeamDisplayTest
from testing_service.test_report import TestReport

class TestHockeyTeamDisplayTest(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 6)
        self.assertEqual(test_report.n_total_tests, 6)

    def test_original_program(self):
        test_report: TestReport = TestReport.parse_test_report(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/original.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 6)

    def test_both_conditions_anded_program(self):
        test_report: TestReport = TestReport.parse_test_report(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/both_conditions_anded.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 6)

    def test_missing_input_program(self):
        test_report: TestReport = TestReport.parse_test_report(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/missing_input.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 6)

    def test_empty_program(self):
        test_report: TestReport = TestReport.parse_test_report(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/empty.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 6)

    def test_semantically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/semantically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 6)

    def test_one_condition_removed_program(self):
        test_report: TestReport = TestReport.parse_test_report(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/one_condition_removed.py"))
        self.assertEqual(test_report.n_successful_tests, 4)
        self.assertEqual(test_report.n_total_tests, 6)
        
    def test_no_ifs_program(self):
        test_report: TestReport = TestReport.parse_test_report(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/no_ifs.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 6)