import unittest
from testing_service.program_tests.adding_to_list_test import AddingToListTest

class TestAddingToList(unittest.TestCase):
    def test_correct_program(self):
        self.assertEqual(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/correct"), (5, 5))
    
    def test_original_program(self):
        self.assertEqual(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/original"), (2, 5))

    def test_missing_output(self):
        self.assertEqual(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/missing_output"), (1, 5))

    def test_syntactically_incorrect_program(self):
        self.assertEqual(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/syntactically_incorrect"), (0, 5))

    def test_semantically_incorrect_program(self):
        self.assertEqual(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/semantically_incorrect"), (0, 5))
    
    def test_missing_append(self):
        self.assertEqual(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/missing_append"), (1, 5))
    
    def test_hard_coded(self):
        self.assertEqual(AddingToListTest.run_tests("tests/testing_service/mock_programs/adding_to_list/hard_coded"), (4, 5))