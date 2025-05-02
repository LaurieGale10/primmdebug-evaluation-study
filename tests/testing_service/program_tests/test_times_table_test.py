import unittest
from testing_service.program_tests.times_table_test import TimesTableTest

class TestTimesTableTest(unittest.TestCase):

    def test_correct_program(self):
        self.assertEqual(TimesTableTest.run_tests("tests/testing_service/mock_programs/times_table/correct"), (3, 3))
    
    def test_original_program(self):
        self.assertEqual(TimesTableTest.run_tests("tests/testing_service/mock_programs/times_table/original"), (1, 3))
    
    def test_syntactically_incorrect_program(self):
        self.assertEqual(TimesTableTest.run_tests("tests/testing_service/mock_programs/times_table/semantically_incorrect"), (1, 3))
    
    def test_correct_printf_formatting(self):
        self.assertEqual(TimesTableTest.run_tests("tests/testing_service/mock_programs/times_table/correct"), (3, 3))

    def test_times_table_hard_coded(self):
        self.assertEqual(TimesTableTest.run_tests("tests/testing_service/mock_programs/times_table/hard_coded"), (1, 3))

    