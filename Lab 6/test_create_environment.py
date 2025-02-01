import pytest
from learning_agent import create_environment

def test_create_environment():
    has_only_1_and_0 = True
    world: list = create_environment()
    assert len(world) == 5
    for i in range(5):
        for j in range(5):
            if world[i][j] != 1 and world[i][j] != 0:
                has_only_1_and_0 = False
        assert has_only_1_and_0

pytest.main(["-v", "test_create_environment.py"])
