from analysis.log_data_analysis.classes.exercise_log import ExerciseLog
from analysis.log_data_analysis.testing_service.test_report import TestReport

import docker
from docker.models.containers import Container
import os.path
import json
import shutil

class DockerInterface:
    """
    A singleton class responsible for managing the Docker container used to run student programs.
    The class is a singleton to ensure all tests take place through the one client that manages a single Docker container.
    """

    _instance: 'DockerInterface' = None

    SHARED_FOLDER_PATH: str = "./data/shared"

    def __init__(self):
        self.client = docker.from_env() #Docker (desktop?) must be running for this line to work

    @staticmethod
    def get_instance() -> 'DockerInterface':
        """Static access method to get the singleton instance of DockerInterface."""
        if DockerInterface._instance is None:
            DockerInterface._instance = DockerInterface()
        return DockerInterface._instance
    
    def create_docker_container(self):
        """
        Create docker container which should:
        Create necessary shared directories
        Copy test files into directory
        Disconnect from network (can this be done programmatically?)
        """ 
        (self._image, logs) = self.client.images.build(path="./analysis/log_data_analysis/testing_service")
        print("Docker image built")
        shared_folder_absolute_path = str(os.path.abspath(f'{self.SHARED_FOLDER_PATH}/'))
        volumes = {
            shared_folder_absolute_path: {
                "bind": "/shared",
                "mode": "rw"
            }
        }
        self._container: Container = self.client.containers.run(image=self._image, detach=True, network_disabled=True, volumes=volumes)
        print("Docker container created")

    def save_student_program(self, student_program: str, student_id: str, exercise_id: str) -> str:
        """
        Return file name it's been saved under in any case?
        """
        #This logic is needed to allow for multiple versions of the same program (in case a student has attempted the same exercise multiple times)
        unique_version_number: int = 1 
        program_filepath: str = f"{self.SHARED_FOLDER_PATH}/student_programs/{exercise_id}_{student_id}_{unique_version_number}.py"
        file_exists: bool = os.path.exists(program_filepath)
        while file_exists:
            unique_version_number += 1
            program_filepath = f"{self.SHARED_FOLDER_PATH}/student_programs/{exercise_id}_{student_id}_{unique_version_number}.py"
            file_exists = os.path.exists(program_filepath)
        with open(program_filepath, "w") as f:
            f.write(student_program)
        return program_filepath

    def run_student_program(self, filename: str, exercise_id: str, normalise_output: bool = False) -> None:
        """
        Run student program in docker container
        Args:
            filename (str): _description_
        """
        # The filepath arguments should relate to the file structure as seen inside the Docker container.
        # Assuming /shared is the mount point inside the container for the host's ./data/shared
        # and student programs are saved in /shared/student_programs/
        container_program_path = f"/shared/student_programs/{os.path.basename(filename)}"

        # Check if the student program file exists inside the container
        self._container.exec_run(
            cmd=["python3", f"/testing_service/program_tests/{exercise_id}_test.py", container_program_path, str(normalise_output)]
        )#TODO: Check whether detached is needed (and whether filepath arguments should relate to Docker container or local mount)

    def get_test_report(self, filename: str) -> TestReport:
        """
        Get test report from student program that was run in run_student_program (stored in /out folder of shared folder)
        Args:
            filename (str): Filename of .out.json file containing test report
        """
        #Check there's an existing .out.json file (otherwise raise a FileNotFoundError)
        #Return contents of the .out.json file
        try:
            with open(filename, "r") as f:
                return TestReport.parse_test_report(json.load(f))
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def test_student_program(self, student_program: str, student_id: str, exercise_id: str, normalise_output: bool = False) -> TestReport:
        """
        Tests a student program by through a series of method calls, representing the following steps:
        - Save the file in the Docker container
        - Running the corresponding test harness program
        - Get the output from the test harness
        The test harnesses run depend on the exercise and can be found in the testing_service/program_test directory.
        """
        program_filename: str = self.save_student_program(student_program, student_id, exercise_id)
        self.run_student_program(program_filename, exercise_id, normalise_output=normalise_output)
        output_file_name: str = os.path.basename(program_filename).replace(".py", ".out.json")
        output_file_path: str = os.path.join(self.SHARED_FOLDER_PATH, "test_results", output_file_name)
        return self.get_test_report(output_file_path)
    
    def close_docker_container(self):
        """
        Close the docker container
        """
        student_programs_path = os.path.join(self.SHARED_FOLDER_PATH, "student_programs")
        test_results_path = os.path.join(self.SHARED_FOLDER_PATH, "test_results")

        for folder in [student_programs_path, test_results_path]:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
        self._container.stop()
        self._container.remove(force=True)
        self.client.close()