import unittest
from testing_service.program_tests.capital_of_hungary_test import CapitalOfHungaryTest

class TestCapitalOfHungaryTest(unittest.TestCase):
    def test_correct_program(self):
        self.assertEqual(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/correct"), (4, 4))

    def test_extended_program(self):
        self.assertEqual(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/extended"), (4, 4))

    def test_logically_incorrect_extended_program(self):
        self.assertEqual(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/logically_incorrect_extended"), (1, 4))
    
    def test_synactically_incorrect_program(self):
        self.assertEqual(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/syntactically_incorrect"), (0, 4))

    def test_empty_program(self):
        self.assertEqual(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/empty"), (0, 4))

    def test_without_if(self):
        self.assertEqual(CapitalOfHungaryTest.run_tests("tests/testing_service/mock_programs/capital_of_hungary/without_if"), (1, 4))