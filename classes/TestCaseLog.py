from classes.ChangeHelpPaneContentEvent import ChangeHelpPaneContentEvent
from classes.ToggleHelpPaneExpansionEvent import ToggleHelpPaneExpansionEvent


class TestCaseLog:
    def __init__(self, expansion_changes: list[ToggleHelpPaneExpansionEvent] = None, pane_content_changes: list[ChangeHelpPaneContentEvent] = None):
        self._expansion_changes = expansion_changes
        self._pane_content_changes = pane_content_changes
    
    @property
    def expansion_changes(self) -> list[ToggleHelpPaneExpansionEvent]:
        return self._expansion_changes
    
    @property
    def pane_content_changes(self) -> list[ChangeHelpPaneContentEvent]:
        return self._pane_content_changes