from enum import Enum

class Hostage:
    # properties
    class _Status(Enum):
        Alive = 0
        Saved = 1
        Killed = 2

    # methods
    def __init__(self, status = "Alive"):
        self.Status = status

    @property
    def status(self):
        return self._Status
    
    @status.setter
    def status(self, value):
        self._Status = value