import funkcje

def test_produkt():
    assert funkcje.product(2, 2) == 4
    assert funkcje.product(4, 4) == 16
    assert funkcje.product(4.5, 5) == 22.5

def test_add():
    assert funkcje.add(7, 3) == 10
    assert funkcje.add(7, -1) == 6
    assert funkcje.add(4.3, 5.3) == 9.6

def test_kwa():
    assert funkcje.kwa(2) == 4
    assert funkcje.kwa(12) == 144
    assert funkcje.kwa(3.5) == 12.25

test_produkt()
test_add()
test_kwa()