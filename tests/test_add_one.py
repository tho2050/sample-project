from sample.simple import add_one


def test_add_one_positive():
    assert add_one(5) == 6


def test_add_one_zero_and_negative():
    assert add_one(0) == 1
    assert add_one(-1) == 0


def test_add_one_large_number():
    assert add_one(10**12) == 10**12 + 1


def test_add_one_float():
    assert add_one(1.5) == 2.5