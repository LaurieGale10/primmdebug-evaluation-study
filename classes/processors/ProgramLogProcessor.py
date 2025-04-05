from classes.ProgramLog import ProgramLog
from enums import IOType
from classes.IOEvent import IOEvent

class ProgramLogProcessor:
    
    @staticmethod
    def get_number_of_inputs(program_log: ProgramLog) -> int:
        return len([io_event for io_event in program_log.io_events if io_event.type == IOType.input])
