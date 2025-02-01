import pytest
from vacuum_cleaner import move_left

action = []
numOfMoves = []


temp1 = action
temp2 = numOfMoves
def test_move_left_pos():
    assert move_left(0, action, numOfMoves) == None and action == temp1 and action == temp2


pytest.main(["-v", "test_move_left.py"])