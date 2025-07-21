from analysis.log_data_analysis.classes.change_pane_content_event import ChangePaneContentEvent
from analysis.log_data_analysis.classes.toggle_pane_expansion_event import TogglePaneExpansionEvent

class TestCaseLog:
    def __init__(self, expansion_changes: list[TogglePaneExpansionEvent] = None, pane_content_changes: list[ChangePaneContentEvent] = None):
        self._expansion_changes: list[TogglePaneExpansionEvent] = expansion_changes
        self._pane_content_changes: list[ChangePaneContentEvent] = pane_content_changes
    
    @property
    def expansion_changes(self) -> list[TogglePaneExpansionEvent]:
        return self._expansion_changes
    
    @property
    def pane_content_changes(self) -> list[ChangePaneContentEvent]:
        return self._pane_content_changes
    
    @staticmethod
    def parse_test_case_log(raw_logs: dict) -> 'TestCaseLog':
        parsed_expansion_changes = None
        if "expansionChanges" in raw_logs:
            parsed_expansion_changes = []
            for raw_expansion_change in raw_logs["expansionChanges"]:
                parsed_expansion_changes.append(TogglePaneExpansionEvent.parse_pane_expansion_log(raw_expansion_change))
        parsed_pane_content_changes = None
        if "paneContentChanges" in raw_logs:
            parsed_pane_content_changes = []
            for raw_pane_content_change in raw_logs["paneContentChanges"]:
                parsed_pane_content_changes.append(ChangePaneContentEvent.parse_pane_content_change_log(raw_pane_content_change))
        return TestCaseLog(
            expansion_changes = parsed_expansion_changes,
            pane_content_changes = parsed_pane_content_changes
        )
    
    def __repr__(self):
        return f'TestCaseLog({self._expansion_changes}, {self._pane_content_changes})'