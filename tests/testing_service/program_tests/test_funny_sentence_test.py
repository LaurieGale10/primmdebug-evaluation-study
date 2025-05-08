import unittest
from testing_service.program_tests.funny_sentence_test import FunnySentenceTest

class TestFunnySentenceTest(unittest.TestCase):

    def test_correct_program(self):
        self.assertEqual(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/correct"), (3, 3))

    def test_orginal_program(self):
        self.assertEqual(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/original"), (0, 3))

    def test_empty_program(self):
        self.assertEqual(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/empty"), (0, 3))
    
    def test_correct_with_concatenation_program(self):
        self.assertEqual(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/correct_with_concatenation"), (3, 3))

    def test_incorrect_output_program(self):
        self.assertEqual(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/incorrect_output"), (1, 3))
    
    def test_hard_coded_program(self):
        self.assertEqual(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/hard_coded"), (2, 3))
    