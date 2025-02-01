import pytest
from utility_agent import pathSelection

world = [
        [0,0,0,0,0,0,0],
        [0,0,0,9,0,0,0],
        [0,1,9,9,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]

row = 2
column = 4
action = []
collect = []
closestObjRow = 2 
closestObjCol = 1

def test_pathSelection():
    path, hurdleAvoided = pathSelection(world, column, row, closestObjRow, closestObjCol)
    assert path == [(2,4),(3,4),(3,3),(3,2),(3,1),(2,1)]
pytest.main(["-v", "test_pathSelection.py"])