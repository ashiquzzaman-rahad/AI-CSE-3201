import pytest
from utility_agent import detectingObjPos

world = [
        [0,0,0,0,0,0,0],
        [0,0,0,9,0,0,0],
        [0,1,9,9,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]

def test_detectingObjPos():
    objPosRow, objPosCol = detectingObjPos(world)
    assert objPosRow == [2] and objPosCol == [1]

pytest.main(["-v", "test_detectingObjPos.py"])