#! python
from math import pi
import sys


def area_circulo(raio):
    return pi * raio ** 2


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("É necessário informar o raio do círculo.")
        print(f"Sintaxe {sys.argv[0][2:]} <raio>")
    else:
        raio = float(sys.argv[1])
        area = area_circulo(raio)
        print(f"A área do círculo é {area}")
