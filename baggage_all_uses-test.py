import pytest
from main import baggage_fee

@pytest.mark.parametrize(
    "w,l,expected,label",
    [
        (-1, 10, "Invalid", "TC1: (1)T -> Invalid"),
        (0, 50, 0,         "TC2: (3)T -> 0"),
        (10, 90, 0,        "TC3: (5)T -> 0"),
        (15, 150, 10,      "TC4: (7)T -> 10"),
        (40, 100, 20,      "TC5: (9)T -> 20"),
        (45, 150, 30,      "TC6: (9)F -> else 30"),
    ]
)
def test_baggage_fee_all_uses_TF(w, l, expected, label):
    assert baggage_fee(w, l) == expected, label
