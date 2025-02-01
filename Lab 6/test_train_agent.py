import pytest
from learning_agent import train_agent

def test_train_agent():
    no_value_axceed_max_train_num: bool = True
    probability: list = train_agent()
    assert len(probability) == 5
    for i in range(5):
        for j in range(5):
            if probability[i][j] < 0 or probability[i][j] > 1000:
                no_value_axceed_max_train_num = False
    assert no_value_axceed_max_train_num

pytest.main(["-v", "test_train_agent.py"])