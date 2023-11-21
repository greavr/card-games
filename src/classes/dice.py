from enum import Enum
import random

class DefaultDice:
    _DiceValues = ["Fail", "Fail", "Fail", "Partial", "Success", "Success"]
    _DiceCount = 1

    # Methods
    def __init__(self, DiceCount: int = 1):
        self._DiceCount = DiceCount

    @property  
    def DiceCount(self):
        return self._DiceCount
    
    @DiceCount.setter
    def DiceCount(self, value:int):
        if value > 0:
            self._DiceCount = value
        else:
            raise ValueError(f"Value must be at least 1")


    # Functions
    def RollDice(self) -> list:
        results = []

        for i in range(self._DiceCount):
            results.append(random.choice(self._DiceValues))
        
        return results