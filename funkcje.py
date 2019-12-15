def add(x, y):
    return x + y


def product(x, y):
    return x * y

def kwa(a):
    return a ** 2

import math


def circle_area(r):
    if r < 0:
        raise ValueError("Promień nie może być ujemny")
    if type(r) not in [int, float]:
        raise TypeError("Promień musi być liczbą")
    return math.pi * r**2