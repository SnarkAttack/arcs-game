from enum import Enum

class PlayerColorEnum(Enum, str):
    RED = 'Red'
    BLUE = 'Blue'
    YELLOW = 'Yellow'
    WHITE = 'White'


class Player():

    def __init__(self, color: PlayerColorEnum):
        self._color = color