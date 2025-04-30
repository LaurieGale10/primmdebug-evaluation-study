from classes.change_pane_content_event import ChangePaneContentEvent
from classes.toggle_pane_expansion_event import TogglePaneExpansionEvent

class HintPaneLog:
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
    def parse_hint_pane_log(raw_logs: dict) -> 'HintPaneLog':
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
        return HintPaneLog(
            expansion_changes = parsed_expansion_changes,
            pane_content_changes = parsed_pane_content_changes
        )

    def __repr__(self):
        return f"HintPaneLog({self.expansion_changes}, {self.pane_content_changes})"