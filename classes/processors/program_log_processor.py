from classes.program_log import ProgramLog
from enums import IOType

class ProgramLogProcessor:
    
    @staticmethod
    def get_number_of_inputs(program_log: ProgramLog) -> int:
        return len([io_event for io_event in program_log.io_events if io_event.type == IOType.input])
    
    @staticmethod
    def get_inputs(program_log: ProgramLog) -> list[str]:
        return [io_event.text for io_event in program_log.io_events if io_event.type == IOType.input]
