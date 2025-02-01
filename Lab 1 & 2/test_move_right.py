import pytest
from vacuum_cleaner import move_right

action = []
numOfMoves = []

def test_move_right_pos0():
    assert move_right(0, action, numOfMoves) == 1 and action == [1] and numOfMoves == [1]

temp1 = action
temp2 = numOfMoves

def test_move_right_pos1():
    assert move_right(1, action, numOfMoves) == None and action == temp1 and action == temp2

pytest.main(["-v", "test_move_right.py"])
