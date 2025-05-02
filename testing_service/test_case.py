class TestCase:
    def __init__(self, inputs: list[str], expected_output: str = None, exception_type: Exception = None):
        self._inputs = inputs
        self._expected_output = expected_output
        self._exception_type = exception_type
    
    @property
    def inputs(self) -> list[str]:
        return self._inputs
    
    @property
    def expected_output(self) -> str:
        return self._expected_output
    
    @property
    def exception_type(self) -> Exception:
        return self._exception_type