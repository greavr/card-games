class Card:
    # Properties
    _card_name = ""
    _card_image_path = ""
    _active = True

    # Methods
    def __init__(self, card_name: str, image_path: str = ""):
        self._card_name = card_name
        self._card_image_path = image_path

    def __str__(self):
        return self._card_name

    @property
    def name(self):
        return self._card_name

    @property
    def image_path(self):
        return self._card_image_path
    
    @property
    def active(self):
        return self._active
    
    # Functions
    def PlayCard(self):
        # Only valid if active
        if not self._active:
            raise ValueError(f"Card Already Played This Round")
        else:
            self._active = False

    def EndRound(self):
        # Place holder function
        self._active = True

# Child Class
class Conversation(Card):
    _card_quote = ""
    _card_cost = 0
    _two_point = {}
    _one_point = {}
    _zero_point = {}
    _other_effects = {}
    _default_values = {}

    def __init__(self, card_name: str, quote: str, cost: int, two_points: dict, one_point: dict, zero_point: dict, default_options: dict, other_effects: dict = {}, image_path: str = "" ):
        Card.__init__(self=self, card_name=card_name, image_path=image_path)
        self._card_quote = quote
        self._card_cost = cost
        self._two_point = two_points
        self._one_point = one_point
        self._zero_point = zero_point
        self._default_values = default_options
        self._other_effects = other_effects

    @property
    def quote(self):
        return self._card_quote

    @property
    def card_cost(self):
        return self._card_cost

    @property
    def default_values(self):
        return self._default_values
    
    @property
    def two_points(self):
        return self._two_point

    @property
    def one_point(self):
        return self._one_point
    
    @property
    def zero_point(self):
        return self._zero_point
    
    @property
    def has_other(self):
        if self._other_effects:
            return True
        else:
            return False
    
    @property
    def other_effects(self):
        return self._other_effects
