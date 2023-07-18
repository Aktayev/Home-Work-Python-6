import pytest
from seasons import  min_at_bd, number_to_words

def test_min_at_bd():
    assert min_at_bd("2023-07-14") == 1440
def test_numer_words():
    assert number_to_words("1440") == "one thousand, four hundred forty"
def test_ext():
    with pytest.raises(SystemExit):
        min_at_bd("june")