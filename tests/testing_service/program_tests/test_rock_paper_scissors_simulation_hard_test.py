import unittest
from testing_service.program_tests.rock_paper_scissors_simulation_hard_test import RockPaperScissorsSimulationHardTest

class TestRockPaperScissorsSimulationHardTest(unittest.TestCase):

    def test_correct_program(self):
        self.assertEqual(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/correct"), (11, 11))
    
    def test_original_program(self):
        self.assertEqual(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/original"), (8, 11))

    def test_hard_coded_random_selection_program(self):
        self.assertEqual(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/hard_coded_random_selection"), (5, 11))

    def test_syntactically_incorrect_program(self):
        self.assertEqual(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/syntactically_incorrect"), (0, 11))
    
    def test_missing_final_print_statement_program(self):
        self.assertEqual(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/missing_final_print_statement"), (1, 11))

    def test_ors_for_winner_checks_program(self):
        self.assertEqual(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/ors_for_winner_checks"), (8, 11))

    def test_no_int_cast_program(self):
        self.assertEqual(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/no_int_cast"), (0, 11))

    def test_printfs_program(self):
        self.assertEqual(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/printfs"), (11, 11))

    def test_no_breaks_program(self):
        self.assertEqual(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/no_breaks"), (1, 11))
    
    def test_no_random_import_program(self):
        self.assertEqual(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/no_random_import"), (1, 11))