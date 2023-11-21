from classes.cards import Conversation

import json

# Load card Functions
def Load_Conversation_Cards(file_path: str) -> list[Conversation]:
    """
    This function parses JSON to create a collection of conversation cards
    Args:
    file_path: str - relative path to json file to load
    Returns:
    list[Conversation] - List of Conversation type cards
    """
    result = []

    # Read Json file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Establish card baseline
    card_defaults = data["default_values"]

    # Itterate over Cards
    for aCard in data["conversations"]:
        newCard = Conversation(
            card_name=aCard["name"],
            quote=aCard["quote"],
            cost=aCard["cost"],
            two_points=aCard["two"],
            one_point=aCard["one"],
            zero_point=aCard["zero"],
            default_options=card_defaults,
            other_effects=aCard["other"]
        )

        result.append(newCard)
    
    #Complete
    return result
