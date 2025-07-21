FROM python:3.13-slim

#Create file structure
COPY program_tests/ /testing_service/program_tests
COPY exercise_test_runner.py testing_service/exercise_test_runner.py
COPY test_case.py testing_service/test_case.py

CMD ["tail", "-f", "/dev/null"]