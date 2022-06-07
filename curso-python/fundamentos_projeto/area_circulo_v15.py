#! python
from math import pi
import sys
import errno


class TerminalColor:
    ERRO = "\033[91m"
    NORMAL = "\033[0m"


def print_error(msg):
    print(TerminalColor.ERRO + msg + TerminalColor.NORMAL)


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
        help()
        print_error("O raio deve ser um valor numérico")
        sys.exit(errno.EINVAL)

    raio = float(sys.argv[1])
    area = area_circulo(raio)
    print(f"A área do círculo é {area}")
