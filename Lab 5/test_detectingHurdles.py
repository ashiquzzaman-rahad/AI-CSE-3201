import pytest
from utility_agent import detectingHurdles

world = [
        [0,0,0,0,0,0,0],
        [0,0,0,9,0,0,0],
        [0,1,9,9,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]

def test_detectingHurdles():
    hurdlePosRow, hurdlePosCol = detectingHurdles(world)
    assert hurdlePosRow == [1,2,2] and hurdlePosCol == [3,2,3]

pytest.main(["-v", "test_detectingHurdles.py"])