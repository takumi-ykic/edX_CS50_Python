from bank import value

def test_value():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("What's up?") == 100
    assert value("hi") == 20

