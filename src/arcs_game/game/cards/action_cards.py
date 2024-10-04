from enum import Enum

class ActionSuitEnum(Enum):
    ADMINISTRATION = 'Administration'
    AGGRESSION = 'Aggression'
    CONSTRUCTION = 'Construction'
    MOBILIZATION = 'Mobilization'

class ActionCard():

    def __init__(self, suit, value, pips):
        self._suit = suit
        self._value = value
        self._pips = pips


SMALL_ACTION_DECK = [
    ActionCard(ActionSuitEnum.ADMINISTRATION, 2, 4),
    ActionCard(ActionSuitEnum.ADMINISTRATION, 3, 3),
    ActionCard(ActionSuitEnum.ADMINISTRATION, 4, 3),
    ActionCard(ActionSuitEnum.ADMINISTRATION, 5, 3),
    ActionCard(ActionSuitEnum.ADMINISTRATION, 6, 2),
    ActionCard(ActionSuitEnum.AGGRESSION, 2, 3),
    ActionCard(ActionSuitEnum.AGGRESSION, 3, 2),
    ActionCard(ActionSuitEnum.AGGRESSION, 4, 2),
    ActionCard(ActionSuitEnum.AGGRESSION, 5, 2),
    ActionCard(ActionSuitEnum.AGGRESSION, 6, 2),
    ActionCard(ActionSuitEnum.CONSTRUCTION, 2, 4),
    ActionCard(ActionSuitEnum.CONSTRUCTION, 3, 3),
    ActionCard(ActionSuitEnum.CONSTRUCTION, 4, 3),
    ActionCard(ActionSuitEnum.CONSTRUCTION, 5, 2),
    ActionCard(ActionSuitEnum.CONSTRUCTION, 6, 2),
    ActionCard(ActionSuitEnum.MOBILIZATION, 2, 4),
    ActionCard(ActionSuitEnum.MOBILIZATION, 3, 3),
    ActionCard(ActionSuitEnum.MOBILIZATION, 4, 3),
    ActionCard(ActionSuitEnum.MOBILIZATION, 5, 2),
    ActionCard(ActionSuitEnum.MOBILIZATION, 6, 2),
]

LARGE_ACTION_DECK = SMALL_ACTION_DECK + [
    ActionCard(ActionSuitEnum.ADMINISTRATION, 1, 4),
    ActionCard(ActionSuitEnum.ADMINISTRATION, 7, 1),
    ActionCard(ActionSuitEnum.AGGRESSION, 1, 3),
    ActionCard(ActionSuitEnum.AGGRESSION, 7, 1),
    ActionCard(ActionSuitEnum.CONSTRUCTION, 1, 4),
    ActionCard(ActionSuitEnum.CONSTRUCTION, 7, 1),
    ActionCard(ActionSuitEnum.MOBILIZATION, 1, 4),
    ActionCard(ActionSuitEnum.MOBILIZATION, 7, 1),
]