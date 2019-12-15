def add(x, y):
    return x + y


def product(x, y):
    return x * y

def test_produkt():
    assert product(2, 2) == 4
    assert product(4, 4) == 16
    assert product(4.5, 5) == 22.5

def test_add():
    assert add(7, 3) == 10
    assert add(7, -1) == 6
    assert add(4.3, 5) == 9.6


test_produkt()
test_add()

