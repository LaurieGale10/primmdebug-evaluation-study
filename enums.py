from enum import Enum

class IOType(Enum):
    error = "error",
    input = "input",
    output = "output"

class DebuggingStage(Enum):
    predict = "predict",
    run = "run",
    spot_defect = "spot_the_defect",
    inspect_code = "inspect_the_code",
    find_error = "find_the_error",
    fix_error = "fix_the_error",
    test = "test",
    completed_test = "completed_test",
    modify = "modify",
    make = "make"

class PaneView(Enum):
    open = "open",
    closed = "closed"

class FocusType(Enum):
    focus_in = "focus_in",
    focus_out = "focus_out"