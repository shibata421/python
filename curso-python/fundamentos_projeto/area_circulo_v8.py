#! python
from math import pi


def circulo(raio):
    area = pi * raio ** 2
    print(f"A área do círculo é {area}")


if __name__ == "__main__":
    raio = float(input("Digite o raio do círculo: "))
    circulo(raio)
