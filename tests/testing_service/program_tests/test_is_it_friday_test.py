import unittest
from testing_service.program_tests.is_it_friday_test import IsItFridayTest

class TestIsItFridayTest(unittest.TestCase):

    def test_correct_program(self):
        self.assertEqual(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/correct"), (3, 3))

    def test_original_program(self):
        self.assertEqual(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/original"), (0, 3))

    def test_semantically_incorrect_program(self):
        self.assertEqual(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/semantically_incorrect"), (0, 3))

    def test_lowercased_friday_program(self):
        self.assertEqual(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/lowercased_friday"), (2, 3))

    def test_missing_if_statement_program(self):
        self.assertEqual(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/missing_if_statement"), (1, 3))

    def test_extended_program(self):
        self.assertEqual(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/extended"), (1, 3)) #Bit of a problem that this is punishes extended solution

    def test_missing_input(self):
        self.assertEqual(IsItFridayTest.run_tests("tests/testing_service/mock_programs/is_it_friday/missing_input"), (1, 3))

if __name__ == '__main__':
    unittest.main()