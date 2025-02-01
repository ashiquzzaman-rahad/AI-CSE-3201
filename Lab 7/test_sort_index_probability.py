import pytest
from reinforment_learning import sort_index_probability

probability: list = [
    [0.500, 0.505, 0.501, 0.510, 0.500],
    [0.511, 0.515, 0.511, 0.519, 0.520],
    [0.500, 0.505, 0.501, 0.510, 0.500],
    [0.511, 0.515, 0.511, 0.519, 0.520],
    [0.500, 0.505, 0.501, 0.510, 0.500],
]

expected_sorted_index: list = [(0,0),(0,4),(2,0),(2,4),(4,0),(4,4),(0,2),(2,2),(4,2),(0,1),(2,1),(4,1),(0,3),(2,3),(4,3),(1,0),(1,2),(3,0),(3,2),(1,1),(3,1),(1,3),(3,3),(1,4),(3,4)]

def test_sort_index_probability():
    sorted_index: list = sort_index_probability(probability)
    assert sorted_index == expected_sorted_index

pytest.main(["-vv", "test_sort_index_probability.py"])