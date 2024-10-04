from abc import ABC
from arcs_game.utilities.exceptions import InvalidActionException

class Piece(ABC):

    def __init__(self, owner, health=2):
        self._owner = owner
        self._health = health

    @property
    def health(self):
        return self._health

    def assign_hit(self):
        # Return True if object must be removed, False otherwise
        self._health -= 1
        if self._health == 0:
            return True
        else:
            return False
        
class Ship(Piece):

    def __init__(self, owner, health=2):
        super().__init__(owner, health)

class Agent(Piece):

    def __init__(self, owner):
        super().__init__(self, owner)

    def assign_hit(self):
        raise InvalidActionException

class _Building(Piece):

    def __init__(self, owner, health=2):
        super().__init__(owner, health)

class City(_Building):

    def __init__(self, owner, health=2):
        super().__init__(owner, health)

class Starport(_Building):

    def __init__(self, owner, health=2):
        super().__init__(owner, health)
    