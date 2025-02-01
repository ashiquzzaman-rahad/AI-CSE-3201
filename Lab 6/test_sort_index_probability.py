import pytest
from learning_agent import sort_index_probability, train_agent

probability: list = [
    [300, 305, 301, 310, 300],
    [311, 315, 311, 319, 320],
    [300, 305, 301, 310, 300],
    [311, 315, 311, 319, 320],
    [300, 305, 301, 310, 300],
]

expected_sorted_index: list = [(0,0),(0,4),(2,0),(2,4),(4,0),(4,4),(0,2),(2,2),(4,2),(0,1),(2,1),(4,1),(0,3),(2,3),(4,3),(1,0),(1,2),(3,0),(3,2),(1,1),(3,1),(1,3),(3,3),(1,4),(3,4)]

def test_sort_index_probability():
    sorted_index: list = sort_index_probability(probability)
    assert sorted_index == expected_sorted_index

pytest.main(["-vv", "test_sort_index_probability.py"])