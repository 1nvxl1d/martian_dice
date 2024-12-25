from src.Hand import Hand

hand = Hand(hand=None, res=[], round_res=['b'], dice_count=10, can_chose_cow=0, can_chose_human=0, can_chose_chicken=1)

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
    Hand.roll_dice(hand)
    Hand.del_tanks(hand)
    assert hand.dice_count == (10 - hand.res.count('t'))
    assert 't' in hand.round_res

def test_chose_beam():
    Hand.roll_dice(hand)
    Hand.chose_beam(hand)
    assert hand.dice_count == (10 - hand.res.count('b'))
    assert 'b' in hand.round_res

def test_chose_human():
    Hand.roll_dice(hand)
    Hand.chose_human(hand)
    assert hand.can_chose_human == 0
    assert hand.dice_count == (10 - hand.res.count('h'))
    assert 'h' in hand.round_res

def test_chose_cow():
    Hand.roll_dice(hand)
    Hand.chose_cow(hand)
    assert hand.can_chose_cow == 0
    assert hand.dice_count == (10 - hand.res.count('c'))
    assert 'c' in hand.round_res

def test_chose_chicken():
    Hand.roll_dice(hand)
    Hand.chose_chicken(hand)
    assert hand.can_chose_chicken == 0
    assert hand.dice_count == (10 - hand.res.count('ch'))
    assert 'ch' in hand.round_res

