import unittest
from testing_service.program_tests.number_timeline_test import NumberTimelineTest

class TestNumberTimelineTest(unittest.TestCase):

    def test_correct_program(self):
        self.assertEqual(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/correct"), (7, 7))

    def test_original_program(self):
        self.assertEqual(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/original"), (5, 7))

    def test_syntactically_incorrect_program(self):
        self.assertEqual(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/syntactically_incorrect"), (0, 7))
    
    def test_semantically_incorrect_program(self):
        self.assertEqual(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/semantically_incorrect"), (2, 7))

    def test_logically_incorrect_program(self):
        self.assertEqual(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/logically_incorrect"), (2, 7))

    def test_different_print_statement_program(self):
        self.assertEqual(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/different_print_statement"), (2, 7)) #Another example of how tests using exact output punishes certain programs
    
    def test_hard_coded_program(self):
        self.assertEqual(NumberTimelineTest.run_tests("tests/testing_service/mock_programs/number_timeline/hard_coded"), (1, 7))