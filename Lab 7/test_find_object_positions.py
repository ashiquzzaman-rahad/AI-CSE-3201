import pytest
from reinforment_learning import find_object_positions

world = [
    [0,0,0,1,0],
    [0,1,0,1,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0]
]

def test_find_object_positions():
    object_pos: list = find_object_positions(world)
    expected_result: list = [(0,3), (1,1), (1,3), (2,1), (3,2), (4,3)]
    assert object_pos == expected_result

pytest.main(["-v", "test_find_object_positions.py"])