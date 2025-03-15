from classes.ExerciseLog import ExerciseLog
from classes.StageLog import StageLog
from enums import DebuggingStage

def format_start_end_times(exercise_log: ExerciseLog) -> ExerciseLog:
    """Reformats the stage and exercise logs such that they contain start and end times to them, making it easier to work out temporal-related data.

    Args:
        exercise_log (ExerciseLog): Exercise log object containing sorted exercise logs.
    """

    #Set first stage log start time (length of stage logs is guaranteed to be at least 1)
    setattr(exercise_log.stage_logs[0], '_start_time', exercise_log.start_time)
    i: int = 1
    while (i < len(exercise_log.stage_logs)) and (exercise_log.stage_logs[i].stage_name != DebuggingStage.exit):
        setattr(exercise_log.stage_logs[i], '_start_time', exercise_log.stage_logs[i - 1].end_time)
        i += 1
    i = len(exercise_log.stage_logs) - 1 if i == len(exercise_log.stage_logs) else i #Reset value of i if too large
    if exercise_log.stage_logs[i].stage_name == DebuggingStage.exit:
        setattr(exercise_log, '_end_time', exercise_log.stage_logs[i].time)
    else:
        setattr(exercise_log, '_end_time', exercise_log.stage_logs[i].end_time)
    return exercise_log