import pytest
from learning_agent import check_performance

world = [
    [0,0,0,1,0],
    [0,1,0,1,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0]
]

probable_sorted_index: list = [(0,0),(0,4),(2,0),(2,4),(4,0),(4,4),(0,2),(2,2),(4,2),(0,1),(2,1),(4,1),(0,3),(2,3),(4,3),(1,0),(1,2),(3,0),(3,2),(1,1),(3,1),(1,3),(3,3),(1,4),(3,4)]


def test_check_performance():
    success, failure = check_performance(world, probable_sorted_index)
    assert success == 24 and failure == 76

pytest.main(["-v", "test_check_performance.py"])