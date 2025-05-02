import unittest
from testing_service.program_tests.school_trip_test import SchoolTripTest

class TestSchoolTripTest(unittest.TestCase):

    def test_correct_program(self):
        self.assertEqual(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/correct"), (6, 6))

    def test_original_program(self):
        self.assertEqual(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/original"), (0, 6))
    
    def test_incorrect_symbol_program(self):
        self.assertEqual(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/incorrect_symbol"), (2, 6))

    def test_incorrect_output_program(self):
        self.assertEqual(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/incorrect_output"), (2, 6))

    def test_syntactically_incorrect_program(self):
        self.assertEqual(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/syntactically_incorrect"), (0, 6))

    def test_hard_coded_program(self):
        self.assertEqual(SchoolTripTest.run_tests("tests/testing_service/mock_programs/school_trip/hard_coded"), (4, 6))
