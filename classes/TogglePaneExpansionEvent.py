from enums import PaneView

class TogglePaneExpansionEvent:
    def __init__(self, new_pane_view: PaneView, time):
        self._new_pane_view = new_pane_view
        self._time = time
    
    @property
    def new_pane_view(self) -> PaneView:
        return self._new_pane_view

    @property
    def time(self):
        return self._time