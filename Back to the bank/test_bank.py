from Bank import value

def test_bank():
    assert value("hello") == "$0"
    assert value("hi") == "$20"
    assert value("what's up") == "$100"
    assert value("Hello") == "$0"
    assert value("HI") == "$20"