from analysis.log_data_analysis.classes.stage_log import StageLog
from analysis.log_data_analysis.classes.exercise_classes.exercise import Exercise
from analysis.log_data_analysis.classes.processors.program_log_processor import ProgramLogProcessor

from analysis.log_data_analysis.enums import DebuggingStage

class StageLogProcessor:
    
    @staticmethod
    def get_time_on_stage(stage_log: StageLog) -> float:
        return (stage_log.end_time - stage_log.start_time).total_seconds() if stage_log.stage_name != DebuggingStage.exit else 0

    @staticmethod
    def get_time_focused(stage_log: StageLog) -> float:
        #Returns time spent focused on the on stage as an absolute value in seconds
        time_not_focused: float = 0
        time_on_stage: float = StageLogProcessor.get_time_on_stage(stage_log)
        if stage_log.focus_events is not None:
            for i in range(0, len(stage_log.focus_events) - 1, 2):
                focus_period = (stage_log.focus_events[i + 1].time - stage_log.focus_events[i].time).total_seconds()
                time_not_focused += focus_period
            return time_on_stage - time_not_focused
        return time_on_stage
    
    @staticmethod
    def does_inspect_the_code_contain_response(stage_log: StageLog) -> bool:
        if stage_log.stage_name != DebuggingStage.inspect_code:
            raise ValueError("Debugging stage for this function must be DebuggingStage.inspect_code")
        return stage_log.response is not None and bool(stage_log.response.strip())
    
    @staticmethod
    def compare_provided_and_student_test_cases(stage_log: StageLog, exercise: Exercise) -> bool:
        """Compares the test cases the student entered with the ones provided in the PRIMMDebug challenge
        Could be done in several ways:
        - Compare number of matching and unmatching test cases
        - Return number of student entered test cases that match the challenge-provided ones
        """
        valid_stages: list[DebuggingStage] = [DebuggingStage.run, DebuggingStage.inspect_code, DebuggingStage.test]
        if stage_log.stage_name not in valid_stages:
            raise ValueError(f"Debugging stage for this function must be run, inspect_code or test, not {DebuggingStage(stage_log.stage_name).value}")

    @staticmethod
    def get_number_of_runs(stage_log: StageLog) -> int:
        valid_stages: list[DebuggingStage] = [DebuggingStage.inspect_code, DebuggingStage.test]
        if stage_log.stage_name not in valid_stages:
            raise ValueError(f"Debugging stage for this function must be inspect_code or test, not {DebuggingStage(stage_log.stage_name).value}")
        return len(stage_log.program_logs) if stage_log.program_logs is not None else 0

    @staticmethod
    def get_time_between_runs(stage_log: StageLog, valid_stages: list[DebuggingStage] = [DebuggingStage.inspect_code, DebuggingStage.test]) -> list[float]:
        if stage_log.stage_name not in valid_stages:
            raise ValueError(f"Debugging stage for this function must be inspect_code or test, not {DebuggingStage(stage_log.stage_name).value}")
        if stage_log.program_logs is None:
            return []
        time_between_runs: list[float] = []
        for i in range(1, len(stage_log.program_logs)):
            time_between_runs.append((stage_log.program_logs[i].timestamp - stage_log.program_logs[i - 1].timestamp).total_seconds())
        return time_between_runs

    @staticmethod
    def get_runs_per_minute(stage_log: StageLog, valid_stages: list[DebuggingStage] = [DebuggingStage.inspect_code, DebuggingStage.test]) -> float:
        if stage_log.stage_name not in valid_stages:
            raise ValueError(f"Debugging stage for this function must be inspect_code or test, not {DebuggingStage(stage_log.stage_name).value}")
        if stage_log.program_logs is None:
            return 0
        number_of_runs: int = len(stage_log.program_logs)
        time_on_runs: float = (stage_log.program_logs[-1].timestamp - stage_log.program_logs[0].timestamp).total_seconds() #Time between first and last run (in seconds)
        return (number_of_runs) / (time_on_runs / 60) if number_of_runs > 1 else 0
    
    @staticmethod
    def get_number_of_inputs_from_runs(stage_log: StageLog, valid_stages: list[DebuggingStage] = [DebuggingStage.run, DebuggingStage.inspect_code, DebuggingStage.test]) -> list[int]:
        if stage_log.stage_name not in valid_stages:
            raise ValueError(f"Debugging stage for this function must be inspect_code or test, not {DebuggingStage(stage_log.stage_name).value}")
        if stage_log.program_logs is None:
            return []
        return [ProgramLogProcessor.get_number_of_inputs(program_log) for program_log in stage_log.program_logs] if stage_log.program_logs is not None else []
    
    @staticmethod
    def get_inputs_from_runs(stage_log: StageLog, valid_stages: list[DebuggingStage] = [DebuggingStage.run, DebuggingStage.inspect_code, DebuggingStage.test]) -> list[list[str]]:
        if stage_log.stage_name not in valid_stages:
            raise ValueError(f"Debugging stage for this function must be inspect_code or test, not {DebuggingStage(stage_log.stage_name).value}")
        if stage_log.program_logs is None:
            return []
        return [ProgramLogProcessor.get_inputs(program_log) for program_log in stage_log.program_logs] if stage_log.program_logs is not None else []