from classes.StageLog import StageLog

class StageLogProcessor:
    
    @staticmethod
    def get_time_on_stage(stage_log: StageLog) -> float:
        return (stage_log.end_time - stage_log.start_time).total_seconds() if stage_log.stage_name != "exit" else None
    