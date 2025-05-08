import unittest
from testing_service.program_tests.lower_to_upper_case_character_conversion_test import LowerToUpperCaseCharacterConversionTest

class TestLowerToUpperCaseCharacterConversionTest(unittest.TestCase):
    
    def test_correct_program(self):
        self.assertEqual(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/correct"), (4, 4))
    
    def test_original_program(self):
        self.assertEqual(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/original"), (2, 4))

    def test_no_return_program(self):
        self.assertEqual(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/no_return"), (0, 4))

    def test_incorrect_inequalities_program(self):
        self.assertEqual(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/incorrect_inequalities"), (3, 4))
    
    def test_anded_condition_program(self):
        self.assertEqual(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/anded_conditon"), (2, 4))

    def test_syntactically_incorrect_program(self):
        self.assertEqual(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/syntactically_incorrect"), (0, 4))
    
    def test_semantically_incorrect_program(self):
        self.assertEqual(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/semantically_incorrect"), (2, 4))
    
    def test_printf_statement_program(self):
        self.assertEqual(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/printf_statement"), (4, 4))
    
    def test_hard_coded_program(self):
        self.assertEqual(LowerToUpperCaseCharacterConversionTest.run_tests("tests/testing_service/mock_programs/lower_to_upper_case_character_conversion/hard_coded"), (3, 4))