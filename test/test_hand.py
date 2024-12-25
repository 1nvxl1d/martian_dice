import pytest

from src.Hand import Hand

hand = Hand(hand=None, res=[], round_res=['b'], dice_count=10, can_chose_cow=0, can_chose_human=0, can_chose_chicken=1)

def test_init():
    assert hand.hand == None
    assert hand.res == []
    assert hand.round_res == ['b']
    assert hand.dice_count == 10
    assert hand.can_chose_cow == 0
    assert hand.can_chose_human == 0
    assert hand.can_chose_chicken == 1

def test_round_start():
    Hand.round_start(hand)
    assert hand.dice_count == 13
    assert hand.round_res == []
    assert hand.can_chose_cow == 1
    assert hand.can_chose_chicken == 1
    assert hand.can_chose_human == 1

def test_roll_dice():
    Hand.roll_dice(hand)
    assert hand.res != []

def test_del_tanks():
    k = hand.dice_count
    Hand.roll_dice(hand)
    Hand.del_tanks(hand)
    assert hand.dice_count == (k - hand.res.count('t'))
    assert 't' in hand.round_res

def test_chose_beam():
    k = hand.dice_count
    Hand.roll_dice(hand)
    Hand.chose_beam(hand)
    assert hand.dice_count == (k - hand.res.count('b'))
    assert 'b' in hand.round_res

def test_chose_human():
    k = hand.dice_count
    Hand.roll_dice(hand)
    Hand.chose_human(hand)
    assert hand.can_chose_human == 0
    assert hand.dice_count == (k - hand.res.count('h'))
    assert 'h' in hand.round_res

def test_chose_cow():
    k = hand.dice_count
    Hand.roll_dice(hand)
    Hand.chose_cow(hand)
    assert hand.can_chose_cow == 0
    assert hand.dice_count == (k - hand.res.count('c'))
    assert 'c' in hand.round_res

def test_chose_chicken():
    k = hand.dice_count
    Hand.roll_dice(hand)
    Hand.chose_chicken(hand)
    assert hand.can_chose_chicken == 0
    assert hand.dice_count == (k - hand.res.count('ch'))
    assert 'ch' in hand.round_res

