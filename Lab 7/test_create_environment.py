import pytest
from reinforment_learning import create_environment, NUM_ROW, NUM_COL

def test_create_environment():
    has_only_1_and_0 = True
    row = NUM_ROW
    col = NUM_COL
    world: list = create_environment()
    assert len(world) == row
    for i in range(row):
        for j in range(col):
            if world[i][j] != 1 and world[i][j] != 0:
                has_only_1_and_0 = False
        assert has_only_1_and_0

pytest.main(["-v", "test_create_environment.py"])
