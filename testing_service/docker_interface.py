class DockerInterface:
    _instance: 'DockerInterface' = None

    @staticmethod
    def get_instance() -> 'DockerInterface':
        """Static access method to get the singleton instance of DockerInterface."""
        if DockerInterface._instance is None:
            DockerInterface._instance = DockerInterface()
        return DockerInterface._instance

    def save_student_program_in_image(self, student_program: str, student_id: str, exercise_id: str):
        pass

    def create_docker_container(self):
        """
        Create docker container which should: create necessary shared directories and copy students' programs for each attempt
        Disconnect from network (can this be done programmatically?)
        """ 
        pass

    def run_tests(self) -> tuple[int, int]:
        """
        Somehow get all the Docker image to run the appropriate tests on each student program in the programs folder
        Give some report of each (could be down with a TestReport class?)
        """
        return (0, 0)