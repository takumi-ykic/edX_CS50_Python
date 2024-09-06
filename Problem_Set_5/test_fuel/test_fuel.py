from fuel import convert, gauge
import pytest

def test_fule():
    assert gauge(convert("100/100")) == "F"
    assert gauge(convert("99/100")) == "F"
    assert gauge(convert("0/100")) == "E"
    assert gauge(convert("1/100")) == "E"
    assert gauge(convert("4/6")) == "67%"
    with pytest.raises(ValueError):
        gauge(convert("one/three"))
    with pytest.raises(ZeroDivisionError):
        gauge(convert("1/0"))



