import unittest
from testing_service.program_tests.hockey_team_display_test import HockeyTeamDisplayTest

class TestAddingToList(unittest.TestCase):
    
    def test_correct_program(self):
        self.assertEqual(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/correct"), (6, 6))
    
    def test_original_program(self):
        self.assertEqual(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/original"), (4, 6))
    
    def test_both_conditions_anded_program(self):
        self.assertEqual(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/both_conditions_anded"), (4, 6))

    def test_missing_input_program(self):
        self.assertEqual(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/missing_input"), (0, 6))

    def test_empty_program(self):
        self.assertEqual(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/empty"), (0, 6))
    
    def test_semantically_incorrect_program(self):
        self.assertEqual(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/semantically_incorrect"), (4, 6))

    def test_one_condition_removed_program(self):
        self.assertEqual(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/one_condition_removed"), (4, 6))
    
    def test_no_ifs_program(self):
        self.assertEqual(HockeyTeamDisplayTest.run_tests("tests/testing_service/mock_programs/hockey_team_display/no_ifs"), (1, 6))