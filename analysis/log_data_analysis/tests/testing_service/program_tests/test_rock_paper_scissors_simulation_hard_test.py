import unittest
from testing_service.program_tests.rock_paper_scissors_simulation_hard_test import RockPaperScissorsSimulationHardTest
from testing_service.test_report import TestReport

class TestRockPaperScissorsSimulationHardTest(unittest.TestCase):
    def test_correct_program(self):
        test_report: TestReport = TestReport.parse_test_report(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/correct.py"))
        self.assertEqual(test_report.n_successful_tests, 11)
        self.assertEqual(test_report.n_total_tests, 11)

    def test_original_program(self):
        test_report: TestReport = TestReport.parse_test_report(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/original.py"))
        self.assertEqual(test_report.n_successful_tests, 8)
        self.assertEqual(test_report.n_total_tests, 11)

    def test_hard_coded_random_selection_program(self):
        test_report: TestReport = TestReport.parse_test_report(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/hard_coded_random_selection.py"))
        self.assertEqual(test_report.n_successful_tests, 5)
        self.assertEqual(test_report.n_total_tests, 11)

    def test_syntactically_incorrect_program(self):
        test_report: TestReport = TestReport.parse_test_report(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/syntactically_incorrect.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 11)

    def test_missing_final_print_statement_program(self):
        test_report: TestReport = TestReport.parse_test_report(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/missing_final_print_statement.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 11)

    def test_ors_for_winner_checks_program(self):
        test_report: TestReport = TestReport.parse_test_report(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/ors_for_winner_checks.py"))
        self.assertEqual(test_report.n_successful_tests, 8)
        self.assertEqual(test_report.n_total_tests, 11)

    def test_no_int_cast_program(self):
        test_report: TestReport = TestReport.parse_test_report(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/no_int_cast.py"))
        self.assertEqual(test_report.n_successful_tests, 0)
        self.assertEqual(test_report.n_total_tests, 11)

    def test_printfs_program(self):
        test_report: TestReport = TestReport.parse_test_report(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/printfs.py"))
        self.assertEqual(test_report.n_successful_tests, 11)
        self.assertEqual(test_report.n_total_tests, 11)

    def test_no_breaks_program(self):
        test_report: TestReport = TestReport.parse_test_report(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/no_breaks.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 11)

    def test_no_random_import_program(self):
        test_report: TestReport = TestReport.parse_test_report(RockPaperScissorsSimulationHardTest.run_tests("tests/testing_service/mock_programs/rock_paper_scissors_simulation_hard/no_random_import.py"))
        self.assertEqual(test_report.n_successful_tests, 1)
        self.assertEqual(test_report.n_total_tests, 11)