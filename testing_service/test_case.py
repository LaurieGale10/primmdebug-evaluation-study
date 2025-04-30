class TestCase:
    def __init__(self, inputs: list[str], expected_output: str):
        self._inputs = inputs
        self._expected_output = expected_output
    
    @property
    def inputs(self) -> list[str]:
        return self._inputs
    
    @property
    def expected_output(self) -> str:
        return self._expected_output