from twttr import shorten
import pytest



def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("python") == "pythn"
    assert shorten("aAeEiIoOuU") == ""
    assert shorten("AEIOUaeiou") == ""
    assert shorten("xyz") == "xyz"
    assert shorten("apple") == "ppl"
    assert shorten("Banana") == "Bnn"
    assert shorten("tWItTeR") == "tWtTR"
def test_empty():
    assert shorten("") == ""

def test_number():
    assert shorten("HELLO123") == "HLL123"

def test_punctuatoin():
    assert shorten("HELLO@!+") == "HLL@!+"


if __name__ == "__main__":
    pytest.main()


