import pytest
from main import baggage_fee

# Các path C2:
# 1) 0T-1
# 2) 0F-2T-3
# 3) 0F-2F-4T-3
# 4) 0F-2F-4F-5T-6
# 5) 0F-2F-4F-5F-7T-8
# 6) 0F-2F-4F-5F-7F-9

@pytest.mark.parametrize(
    "weight,length,expected",
    [
        pytest.param(-10, -10, "Invalid", id="1:0T-1 -> Invalid"),
        pytest.param(0, 0, 0, id="2:0F-2T-3 -> 0"),
        pytest.param(10, 10, 0, id="3:0F-2F-4T-3 -> 0"),
        pytest.param(20, 150, 10, id="4:0F-2F-4F-5T-6 -> 10"),
        pytest.param(30, 10, 20, id="5:0F-2F-4F-5F-7T-8 -> 20"),
        pytest.param(30, 150, 30, id="6:0F-2F-4F-5F-7F-9 -> 30"),
    ],
)
def test_baggage_fee_c2_paths(weight, length, expected):
    assert baggage_fee(weight, length) == expected
