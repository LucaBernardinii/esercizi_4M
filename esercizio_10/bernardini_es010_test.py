from bernardini_es010.py import Frazione 


def test_add():
    f1 = Frazione(3, 4)
    f2 = Frazione(2, 4)
    f3 = f1 + f2
    assert str(f3) == "Frazione(5, 4)"


def test_sub():
    f1 = Frazione(3, 4)
    f2 = Frazione(2, 4)
    f4 = f1 - f2
    assert str(f4) == "Frazione(1, 4)"


def test_mul():
    f1 = Frazione(3, 4)
    f2 = Frazione(2, 4)
    f5 = f1 * f2
    assert str(f5) == "Frazione(6, 16)"


def test_str():
    f1 = Frazione(3, 4)
    assert str(f1) == "Frazione(3, 4)"