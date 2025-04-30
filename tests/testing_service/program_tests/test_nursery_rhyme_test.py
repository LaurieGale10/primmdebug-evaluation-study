import unittest
from testing_service.program_tests.nursery_rhyme_test import NurseryRhymeTest

class TestNurseryRhymeTest(unittest.TestCase):

    def test_correct_program(self):
        self.assertEqual(NurseryRhymeTest.run_tests("tests/testing_service/mock_programs/nursery_rhyme/correct_implementation"), (1, 1))

    def test_original_program(self):
        self.assertEqual(NurseryRhymeTest.run_tests("tests/testing_service/mock_programs/nursery_rhyme/original_implementation"), (0, 1))

    def test_logically_incorrect_program(self):
        self.assertEqual(NurseryRhymeTest.run_tests("tests/testing_service/mock_programs/nursery_rhyme/logically_incorrect_implementation"), (0, 1))

if __name__ == '__main__':
    unittest.main()