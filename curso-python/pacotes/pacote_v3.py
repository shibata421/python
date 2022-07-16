#!/usr/bin/python3
from pacote1 import modulo1
from pacote2 import modulo1 as modulo1_sub


if __name__ == "__main__":
    print(modulo1.soma(1, 1))
    print(modulo1_sub.subtracao(1, 1))