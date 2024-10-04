from arcs_game.game.cards.action_cards import (ActionCard,
                                               SMALL_ACTION_DECK,
                                               LARGE_ACTION_DECK)

def test_small_action_deck():

    assert len(SMALL_ACTION_DECK) == 20

def test_large_action_deck():

    assert len(LARGE_ACTION_DECK) == 28