#! python
from math import pi
import sys


def area_circulo(raio):
    return pi * raio ** 2


if __name__ == "__main__":
    raio = float(sys.argv[1])
    area = area_circulo(raio)
    print(f"A área do círculo é {area}")
