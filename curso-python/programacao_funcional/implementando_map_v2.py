#!/usr/bin/python3
def mapear(funcao, tupla):
    return (funcao(num) for num in tupla)


if __name__ == "__main__":
    numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    print(list(mapear(lambda x: x * 2, numeros)))
    print(tuple(mapear(lambda x: x ** 2, numeros)))
