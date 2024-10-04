from abc import ABC, abstractmethod

class _System(ABC):

    def __init__(self, id):
        # System ID will be the notation described in the README's "Notation" section
        self._id = id
        self._ships = []

    @abstractmethod
    def get_free_spaces(self):
        raise NotImplementedError

class _Planet(_System, ABC):

    def __init__(self, resource):
        self._resource = resource

    @property
    def resource(self):
        return self._resource
    
    @abstractmethod
    def add_building(self, building):
        # TODO: Check if building player controls system, building is damaged if
        # they do NOT
        raise NotImplementedError

class _PlanetOneBuilding(_Planet):

    def __init__(self, resource):
        super().__init__(resource)
        self._building_slot_1 = None

    def get_free_spaces(self):
        return 1 if self._building_slot_1 is None else 0
    
    def add_building(self, building):
        if self.get_free_spaces() == 0:
            # TODO: Craft specific exceptions
            raise Exception
        else:
            self._building_slot_1 = building

class _PlanetTwoBuildings(_Planet):

    def __init__(self, resource):
        super().__init__(resource)
        self._building_slot_1 = None
        self._building_slot_2 = None

    def get_free_spaces(self):
        return (1 if self._building_slot_1 is None else 0 
                + 1 if self._building_slot_2 is None else 0)
    
    def add_building(self, building):
        if self.get_free_spaces() == 0:
            raise Exception
        if self._building_slot_1 == None:
            self._building_slot_1 = building
        elif self._building_slot_2 == None:
            self._building_slot_1 = building

class _Gate(_System):

    def __init__(self):
        pass

    def get_free_spaces(self):
        return 0

class _Cluster():

    def __init__(self, id):
        # Cluster ID is a number 1 through 6, as indicated on the game board
        self._id = id

class ArcsBoard():

    # Adjacency notes: 2H and 3T are adjacent, as are 5H and 6T, if both relevant clusters
    # are in the game

    def __init__(self):
        pass

