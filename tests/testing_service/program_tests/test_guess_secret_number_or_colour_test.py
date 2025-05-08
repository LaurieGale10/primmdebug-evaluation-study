import unittest
from testing_service.program_tests.guess_secret_number_or_colour_test import GuessSecretNumberOrColourTest

class TestGuessSecretNumberOrColourTest(unittest.TestCase):
    def test_correct_program(self):
        self.assertEqual(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/correct"), (6, 6))
    
    def test_original_program(self):
        self.assertEqual(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/original"), (5, 6))
    
    def test_syntactically_incorrect_program(self):
        self.assertEqual(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/syntactically_incorrect"), (0, 6))

    def test_missing_final_output_program(self):
        self.assertEqual(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/missing_final_output"), (0, 6))

    def test_incorrect_inequality_program(self):
        self.assertEqual(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/incorrect_inequality"), (3, 6))
    
    def test_semantically_incorrect_program(self):
        self.assertEqual(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/semantically_incorrect"), (4, 6))
    
    def test_incorrect_assignments_program(self):
        self.assertEqual(GuessSecretNumberOrColourTest.run_tests("tests/testing_service/mock_programs/guess_secret_number_or_colour/incorrect_assignments"), (1, 6))