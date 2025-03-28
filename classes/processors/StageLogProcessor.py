from classes.StageLog import StageLog
from enums import DebuggingStage

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