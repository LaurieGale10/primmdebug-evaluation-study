class TestCase:
    def __init__(self, expected: str, input: list[str] = None, actual: str = None):
            self._expected: str = expected
            self._input: str = input
            self._actual: str = actual
    
    @property
    def expected(self) -> str:
        return self._expected

    @property
    def input(self) -> str:
        return self._input if self._input is not None else None

    @property
    def actual(self) -> str:
        return self._actual if self._actual is not None else None
    
    @staticmethod
    def parse_test_case(raw_data: dict) -> 'TestCase':
        return TestCase(
             expected = raw_data["expected"],
             input = raw_data.get("input"),
             actual = raw_data.get("actual")
        )