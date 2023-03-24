from Plates import is_valid

def test_plates():
    assert is_valid("ab1234") == True
    assert is_valid("PH1234") == True
    assert is_valid("abc") == True
    assert is_valid("12") == False
    assert is_valid("ab12347") == False
    assert is_valid("ab1234") == True
    assert is_valid("abcde1") == True
    assert is_valid("a") == False
    assert is_valid("4") == False