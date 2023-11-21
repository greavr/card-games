from cards import Card

class Player:
    # Properties
    _current_hand = []

    # methods
    def __init__(self, cards:list = []):
        self.Properties = cards

    @property
    def CardList(self):
        return self._cards

    # Functions
    def AddCard(self, new_card: Card):
        self._current_hand.append(new_card)
    
    def RemoveCard(self, remove_card: Card):
        if remove_card in self._current_hand:
            self._current_hand.remove(remove_card)
        else:
            raise ValueError(f"Card {remove_card.name} not found in hand: {self._current_hand}")
        
    def PlayCard(self, play_card: Card):
        pass

    def BurnCard(self, play_cards: list[Card]):
        pass
