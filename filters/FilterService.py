from classes.ExerciseLog import ExerciseLog
from classes.StageLog import StageLog
from classes.StudentId import StudentId

class FilterService:

    @staticmethod
    def filter_student_ids_by_school(student_ids: list[StudentId], school: str) -> list[StudentId]:
        if not school:
            raise ValueError("The 'school' argument must be defined.")
        filtered_student_ids: list[StudentId] = [student_id for student_id in student_ids if student_id.school == school]
        return filtered_student_ids

    @staticmethod
    def filter_exercise_logs_by_student_ids(exercise_logs: list[ExerciseLog], student_ids: list[StudentId]) -> list[ExerciseLog]:
        student_id_strings: list[str] = [student_id.id for student_id in student_ids if hasattr(student_id, "date_first_accessed")]
        return [exercise_log for exercise_log in exercise_logs if exercise_log.student_id in student_id_strings]
    
    @staticmethod
    def filtered_stage_logs_from_exercise_logs(exercise_logs: list[ExerciseLog]) -> list[StageLog]:
        """Generates a list of stage logs that exist within a passed in list of exercise logs.
        Useful for filtering stage logs by school, as this cannot be done directly from a list of stage logs

        Args:
            exercise_logs (list[ExerciseLog]): A list of exercise logs to generate a list of stage logs from (filtered by school)

        Returns:
            list[StageLog]: A list of stage logs that exist within the passed in list of exercise logs
        """
        return [stage_log for exercise_log in exercise_logs for stage_log in exercise_log.stage_logs]