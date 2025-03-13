from classes.ExerciseLog import ExerciseLog
from classes.StageLog import StageLog
from enums import DebuggingStage

class ExerciseLogProcessor:
    
    @staticmethod
    def get_last_stage(exercise_log: ExerciseLog) -> StageLog:
        #Need to sort list by overall stage number and get name of last one. UPDATE: Should be done in StageLog now
        exercises_stages: list[StageLog] = exercise_log.stage_logs
        exercises_stages = [stage for stage in exercises_stages if stage.stage_name != "exit"]
        #Remove exit logs as they don't contain a overall_stage_number property
        if len(exercises_stages) > 0:
            exercises_stages.sort(key=lambda x : x.overall_stage_number)
            return(exercises_stages[len(exercises_stages) - 1])
        return None
    
    @staticmethod
    def is_error_reportedly_solved() -> bool:
        pass
    """How to tell if an exercise has definitely been successfully completed:
    - Test harnesses
    - If a students' transitions are test --> modify
    
    How to tell if a student definitely hasn't successfully completed an exercise
    - Test --> Find the error
    - Test --> Inspect the code"""
    
    @staticmethod
    def get_time_on_exercise(exercise_log: ExerciseLog) -> float:
        return (exercise_log.end_time - exercise_log.start_time).total_seconds()
    
    @staticmethod
    def get_written_responses(exercise_log: ExerciseLog) -> list[str]:
        responses: list[str] = []
        for stage_log in exercise_log.stage_logs:
            if stage_log.stage_name in [DebuggingStage.predict, DebuggingStage.spot_defect, DebuggingStage.inspect_code, DebuggingStage.fix_error]:
                responses.append(stage_log.response)
        return responses