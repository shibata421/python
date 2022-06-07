#! python
from math import pi
import sys
import errno


def area_circulo(raio):
    return pi * raio ** 2


def help():
    print("É necessário informar o raio do círculo.")
    print(f"Sintaxe {sys.argv[0][2:]} <raio>")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        print("O raio deve ser um valor numérico")
        help()
        sys.exit(errno.EINVAL)

    raio = float(sys.argv[1])
    area = area_circulo(raio)
    print(f"A área do círculo é {area}")
