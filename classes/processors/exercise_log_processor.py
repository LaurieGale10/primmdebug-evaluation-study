from classes.program_log import ProgramLog
from classes.exercise_log import ExerciseLog
from classes.stage_log import StageLog
from classes.processors.stage_log_processor import StageLogProcessor
from classes.written_response import WrittenResponse

from testing_service.test_report import TestReport
from testing_service.docker_interface import DockerInterface
from enums import DebuggingStage

from statistics import median

class ExerciseLogProcessor:

    @staticmethod
    def get_exercise_log_by_id(exercise_log_id: str, exercise_logs: list[ExerciseLog]) -> ExerciseLog | None:
        """Returns the exercise log with the given ID from a list of exercise logs.

        Args:
            exercise_log_id (str): The ID of the exercise log to return.
            exercise_logs (list[ExerciseLog]): The list of exercise logs to search in.

        Returns:
            ExerciseLog: The exercise log with the given ID, or None if no such log exists.
        """
        return next((log for log in exercise_logs if log.id == exercise_log_id), None)

    @staticmethod
    def get_stage_names(exercise_log: ExerciseLog) -> list[str]:
        return [DebuggingStage(stage.stage_name).value for stage in exercise_log.stage_logs]
    
    @staticmethod
    def get_last_stage(exercise_log: ExerciseLog) -> StageLog:
        #Need to sort list by overall stage number and get name of last one. UPDATE: Should be done in StageLog now
        exercises_stages: list[StageLog] = exercise_log.stage_logs
        exercises_stages = [stage for stage in exercises_stages if stage.stage_name.value != "exit"]
        #Remove exit logs as they don't contain a overall_stage_number property
        if len(exercises_stages) > 0:
            exercises_stages.sort(key=lambda x : x.overall_stage_number)
            return(exercises_stages[len(exercises_stages) - 1])
        return None
    
    @staticmethod
    def is_error_reportedly_solved() -> bool:
        pass

    @staticmethod
    def get_last_program_log(exercise_log: ExerciseLog) -> ProgramLog | None:
        """Returns the last program log from the exercise log.

        Args:
            exercise_log (ExerciseLog): The exercise log to get the last program log from.

        Returns:
            ProgramLog: The final (last executed) program log in the exercise log. If there aren't any program logs, None is returned.
        """

        stages_with_program_logs: list[DebuggingStage] = [DebuggingStage.run, DebuggingStage.inspect_code, DebuggingStage.fix_error, DebuggingStage.test]
        for i in range(len(exercise_log.stage_logs) - 1, -1, -1):
            stage_log = exercise_log.stage_logs[i]
            if stage_log.stage_name in stages_with_program_logs and stage_log.program_logs is not None:
                return stage_log.program_logs[-1]
        return None
    
    def get_time_per_stage(exercise_log: ExerciseLog, take_median: bool = True) -> dict[DebuggingStage, float]:
        """Calculates the total time spent on each PRIMMDebug stage during the challenge attempt.

        If a stage has been completed multiples times, the culumative time on that stage is calculated if take_median is False, or the median time otherwise.

        Args:
            exercise_log (ExerciseLog): The exercise log to calculate the time per stage for.
            take_median (bool, optional): Whether to calculate the median or total time on a particular stage. Defaults to False.

        Returns:
            dict[DebuggingStage, float]: A matrix of time per stage and the time for each 
        """
        #Originally store all times for a stage in a list, then either take the median or sum them up depending on take_median
        times_per_individual_stage: dict[DebuggingStage, list[float]] = {stage: [] for stage in DebuggingStage}
        for stage_log in exercise_log.stage_logs:
            if stage_log.stage_name != DebuggingStage.exit:
                times_per_individual_stage[stage_log.stage_name].append(StageLogProcessor.get_time_on_stage(stage_log))
        time_per_stage: dict[DebuggingStage, float] = {stage: 0 for stage in DebuggingStage}
        for (stage, times) in times_per_individual_stage.items():
            if len(times) > 0:
                time_per_stage[stage] = median(times) if take_median else sum(times)
            else:
                time_per_stage[stage] = 0
        return time_per_stage
    
    @staticmethod
    def get_first_find_the_error_stage(exercise_log: ExerciseLog) -> StageLog | None:
        """Returns the first Find the Error stage in the exercise log, or None if no such stage exists.

        Args:
            exercise_log (ExerciseLog): The exercise log to search in.

        Returns:
            StageLog: The first Find the Error stage in the exercise log, or None if no such stage exists.
        """
        for stage_log in exercise_log.stage_logs:
            if stage_log.stage_name == DebuggingStage.find_error:
                return stage_log
        return None
    
    @staticmethod
    def does_find_the_error_stage_have_correct_response(exercise_log: ExerciseLog) -> bool:
        """Checks whether the first Find the Error stage in the exercise log has a correct response.

        Args:
            exercise_log (ExerciseLog): The exercise log to check.

        Returns:
            bool: True if the first Find the Error stage has a correct response, False otherwise.
        """
        first_find_the_error_stage = ExerciseLogProcessor.get_first_find_the_error_stage(exercise_log)
        return first_find_the_error_stage.correct if first_find_the_error_stage is not None and first_find_the_error_stage.correct is not None else None

    @staticmethod
    def is_final_program_erroneous(exercise_log: ExerciseLog) -> bool:
        last_program_log = ExerciseLogProcessor.get_last_program_log(exercise_log)
        return last_program_log.compiled if last_program_log is not None else None

    @staticmethod
    def get_time_on_exercise(exercise_log: ExerciseLog) -> float:
        return (exercise_log.end_time - exercise_log.start_time).total_seconds()

    @staticmethod
    def get_written_responses(exercise_log: ExerciseLog) -> list[str]:
        responses: list[str] = []
        for stage_log in exercise_log.stage_logs:
            if stage_log.stage_name in [DebuggingStage.predict, DebuggingStage.spot_defect, DebuggingStage.inspect_code, DebuggingStage.fix_error]:
                if stage_log.response is not None and bool(stage_log.response.strip()):
                    responses.append(stage_log.response)
        return responses
    
    @staticmethod
    def get_time_focused(exercise_log: ExerciseLog) -> float:
        #Returns time spent focused on exercise as a percentage of time spent on exercise
        time_focused: float = 0
        time_on_exercise: float = ExerciseLogProcessor.get_time_on_exercise(exercise_log)
        for stage_log in exercise_log.stage_logs:
            time_focused_on_stage = StageLogProcessor.get_time_focused(stage_log)
            time_focused += time_focused_on_stage
        return (time_focused / time_on_exercise) * 100
    

    @staticmethod
    def were_test_cases_viewed(exercise_log: ExerciseLog, stages: list[DebuggingStage] = [DebuggingStage.inspect_code, DebuggingStage.test]) -> bool:
        """Checks whether the test case panes were viewed at any point during the PRIMMDebug exercise
        (i.e., in any of the PRIMMDebug stages that displayed the test case pane)

        Args:
            exercise_log (ExerciseLog): The exercise_log to perform the function on
            stages (list[DebuggingStage], optional): The stages to check for test case pane views. Defaults to [DebuggingStage.inspect_code, DebuggingStage.test]. Other valid arguments are just [DebuggingStage.inspect_code] or [DebuggingStage.test] 

        Returns:
            bool: A bool value indicating whether a test case pane was viewed at any point during the exercise. Returns None if the exercise doesn't contain test case pane.
        """
        relevant_exercise_stages: list[StageLog] = [stage for stage in exercise_log.stage_logs if stage.stage_name in stages]
        for stage in relevant_exercise_stages:
            if stage.test_case_logs is not None:
                return True
        return False

    @staticmethod
    def did_exercise_move_to_modify(exercise_log: ExerciseLog) -> bool:
        return ExerciseLogProcessor.get_last_stage(exercise_log).stage_name == "modify"
    
    @staticmethod
    def test_final_program(exercise_log: ExerciseLog, docker_interface: DockerInterface, normalise_output: bool = False) -> TestReport | None:
        """Tests the last snapshot from an exercise log.
        This is done by running the student program on a Docker container, accessed through the DockerInterface class.

        Args:
            exercise_log (ExerciseLog): The exercise log containing a snapshot to be tested.

        Returns:
            TestReport: A TestReport object containing the number of passed tests and the total number of tests ran.
            If exercise_log doesn't contain any program logs, None is returned.
        """
        #Get last program
        last_program_log: ProgramLog = ExerciseLogProcessor.get_last_program_log(exercise_log)
        if last_program_log is None:
            return None
        last_program_string: str = last_program_log.snapshot
        #Return the run_tests function for the exercise class name+Test
        return docker_interface.test_student_program(last_program_string, exercise_log.student_id, exercise_log.exercise_name, normalise_output=normalise_output)