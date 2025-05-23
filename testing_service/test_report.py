class TestReport:

    def __init__(self, n_successful_tests: int, n_total_tests: int):
        self._n_successful_tests: int = n_successful_tests
        self._n_total_tests: int = n_total_tests

    @property
    def n_successful_tests(self) -> int:
        return self._n_successful_tests
    
    @property
    def n_total_tests(self) -> int:
        return self._n_total_tests
    
    @staticmethod
    def parse_test_report(raw_report: dict[str]):
        """
        Parse a test report from a dictionary to a TestReport object.
        Args:
            raw_report (dict[str]): The raw test report data.
        Returns:
            TestReport: The parsed test report object.
        """
        return TestReport(
            n_successful_tests = raw_report["successful_tests"],
            n_total_tests = raw_report["total_tests"]
        )