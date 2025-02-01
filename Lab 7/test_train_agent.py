import pytest
from reinforment_learning import train_agent, NUM_ROW, NUM_COL

def test_train_agent():
    no_value_exceed_max_train_num: bool = True
    probability: list = train_agent()
    assert len(probability) == 5
    for i in range(NUM_ROW):
        for j in range(NUM_COL):
            if probability[i][j] < 0 or probability[i][j] > 1:
                no_value_exceed_max_train_num = False
    assert no_value_exceed_max_train_num

pytest.main(["-v", "test_train_agent.py"])