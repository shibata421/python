#! python
from math import pi


def area_circulo(raio):
    return pi * raio ** 2


if __name__ == "__main__":
    raio = float(input("Digite o raio do círculo: "))
    area = area_circulo(raio)
    print(f"A área do círculo é {area}")
