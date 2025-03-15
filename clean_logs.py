from classes.ExerciseLog import ExerciseLog
from classes.StageLog import StageLog
from classes.WindowFocusEvent import WindowFocusEvent
from enums import DebuggingStage, FocusType

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

def clean_focus_events(stage_log: StageLog) -> StageLog:
    """Take focus event of of a nature (i.e. focus_out or focus_in) and remove all succeeding focus events of the same value."""
    if stage_log.focus_events is not None:
        cleaned_focus_events: list[WindowFocusEvent] = []
        i: int = 1
        current_focus_value: FocusType = stage_log.focus_events[0].focus
        cleaned_focus_events.append(stage_log.focus_events[0])
        while (i < len(stage_log.focus_events)):
            if stage_log.focus_events[i].focus != current_focus_value:
                cleaned_focus_events.append(stage_log.focus_events[i])
                current_focus_value = stage_log.focus_events[i].focus
            i += 1
        stage_log.focus_events = cleaned_focus_events
    return stage_log