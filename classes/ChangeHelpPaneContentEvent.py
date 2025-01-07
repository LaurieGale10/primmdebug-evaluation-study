class ChangeHelpPaneContentEvent:
    def __init__(self, new_content: str, time):
        self._new_content = new_content
        self._time = time

    @property
    def new_content(self):
        return self._new_content
    
    @property
    def time(self):
        return self._time