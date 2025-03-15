from bank import value
import pytest

def test_value():
    assert ("Hello") == "$0"
    assert ("hello") == "$0"
    assert ("What's up?") == "$100"
    assert ("how good you are!") == "$20"


