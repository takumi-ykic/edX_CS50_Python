from um import count

def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2
    assert count("yum") == 0
