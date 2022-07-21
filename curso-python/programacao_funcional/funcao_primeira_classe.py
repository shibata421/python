#!/usr/bin/python3


def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


if __name__ == "__main__":
    # Retornar alternadamente o dobro e o quadrado nos números de 1 a 10
    funcs = [dobro, quadrado] * 5

    for funcao, numero in zip(funcs, range(1, 11)):
        print(f'O {funcao.__name__} de {numero} é {funcao(numero)}')
