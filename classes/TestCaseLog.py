from classes.ChangePaneContentEvent import ChangePaneContentEvent
from classes.TogglePaneExpansionEvent import TogglePaneExpansionEvent


class TestCaseLog:
    def __init__(self, expansion_changes: list[TogglePaneExpansionEvent] = None, pane_content_changes: list[ChangePaneContentEvent] = None):
        self._expansion_changes = expansion_changes
        self._pane_content_changes = pane_content_changes
    
    @property
    def expansion_changes(self) -> list[TogglePaneExpansionEvent]:
        return self._expansion_changes
    
    @property
    def pane_content_changes(self) -> list[ChangePaneContentEvent]:
        return self._pane_content_changes