from enum import Enum

class DefaultBoard:
    # properties
    _ThreatLevel = ""
    _Hostages = []
    _ConversationPoints = 0
    _ThreatMap ={
        "S" : 3,
        "1" : 3,
        "2" : 2,
        "3" : 2,
        "4" : 2,
        "5" : 2,
        "6" : 2,
        "K" : 1
    }

    #methods
    def __init__(self, ConversationPoints: int = 0, ThreatLevel: str = "", Hostages: list = []):
        self._ConversationPoints = ConversationPoints
        self._ThreatLevel = ThreatLevel
        self._Hostages = Hostages
    
    @property
    def ThreatLevel(self):
        return self._ThreatLevel
    
    @ThreatLevel.setter
    def ThreatLevel(self, value: str):
        # Validate value is in range
        if value in self._ThreatMap:
            self._ThreatLevel = value
        else:
            raise ValueError(f"Value must be string from following values: {self._ThreatMap.keys()}")
    
    @property
    def ConversationPoints(self):
        return self._ConversationPoints
    
    @ConversationPoints.setter
    def ConversationPoints(self, value: int):
        self._ConversationPoints = value
    
    
    @property
    def Hostages(self):
        return self._Hostages
    
    @Hostages.setter
    def Hostages(self, value: list):
        self._Hostages = value
    
    @property
    def ThreatMap(self):
        return self._ThreatMap.keys()
    
    # Board Functions
    def DiceCount(self):
        return self._ThreatMap[self.ThreatLevel]



