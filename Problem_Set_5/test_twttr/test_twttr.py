from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("cs50") == "cs50"
    assert shorten("abex") == "bx"
    assert shorten("AbEx") == "bx"
    assert shorten("cis.cis") == "cs.cs"
