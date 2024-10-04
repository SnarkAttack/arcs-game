import pytest
from arcs_game.game.pieces import Ship, Agent, City, Starport
from arcs_game.utilities.exceptions import InvalidActionException

def test_damage_healthy_ship():

    ship = Ship(None)
    is_destroyed = ship.assign_hit()
    assert is_destroyed == False
    assert ship.health == 1

def test_damage_damaged_ship():

    ship = Ship(None, health=1)
    is_destroyed = ship.assign_hit()
    assert is_destroyed == True

def test_damage_agent():
    
    agent = Agent(None)
    with pytest.raises(InvalidActionException) as excinfo:
        agent.assign_hit()
    assert str(excinfo.value) == "Invalid action"

def test_damage_healthy_building():

    city = City(None)
    is_destroyed = city.assign_hit()
    assert is_destroyed == False
    assert city.health == 1

def test_damage_damaged_building():

    starport = Starport(None, health=1)
    is_destroyed = starport.assign_hit()
    assert is_destroyed == True