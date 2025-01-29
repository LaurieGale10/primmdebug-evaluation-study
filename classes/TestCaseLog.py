from classes.ChangePaneContentEvent import ChangePaneContentEvent
from classes.TogglePaneExpansionEvent import TogglePaneExpansionEvent


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
        if (raw_logs["expansionChanges"]):
            parsed_expansion_changes = []
            for raw_expansion_change in raw_logs["expansionChanges"]:
                parsed_expansion_changes.append(TogglePaneExpansionEvent.parse_pane_expansion_log(raw_expansion_change))
        if (raw_logs["paneContentChanges"]):
            parsed_pane_content_changes = []
            for raw_pane_content_change in raw_logs["paneContentChanges"]:
                parsed_pane_content_changes.append(ChangePaneContentEvent.parse_pane_content_change_log(raw_pane_content_change))
        return TestCaseLog(
            expansion_changes = parsed_expansion_changes if parsed_expansion_changes is not None else None,
            pane_content_changes = parsed_pane_content_changes if parsed_pane_content_changes is not None else None
        )
    
    def __repr__(self):
        return f'TestCaseLog({self._expansion_changes}, {self._pane_content_changes})'