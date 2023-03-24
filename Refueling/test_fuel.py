from fuel import convert, gauge

def test_fuel():
    assert convert("100/50") == ValueError
    assert convert("a") == ValueError
    assert convert("50/100") == 50
    assert convert("25/100") == 25
    assert convert("38/80") == 48
    assert convert("25/0") == ZeroDivisionError
    assert convert("100/100") == 100

def test_gauge():
    assert gauge(100) == 'F'
    assert gauge(1) == 'E'
    assert gauge(50) == '50%'
    assert gauge(48) == '48%'