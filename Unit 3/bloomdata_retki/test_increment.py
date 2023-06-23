def increment(num):
    return num + 1

def test_increment():
    assert increment(1) == 2
    assert increment(100) == 101

def test_increment_neg():
    assert increment(-10) == -9

def test_increment_float():
    assert increment(3.14) == 4.14