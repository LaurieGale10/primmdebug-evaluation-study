import unittest
from testing_service.program_tests.funny_sentence_test import FunnySentenceTest

class TestFunnySentenceTest(unittest.TestCase):

    def test_correct_program(self):
        self.assertEqual(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/correct"), (3, 3))

    def test_orginal_program(self):
        self.assertEqual(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/original"), (0, 3))
    
    def test_correct_with_concatenation_program(self):
        self.assertEqual(FunnySentenceTest.run_tests("tests/testing_service/mock_programs/funny_sentence/correct_with_concatenation"), (3, 3))


if __name__ == '__main__':
    unittest.main()