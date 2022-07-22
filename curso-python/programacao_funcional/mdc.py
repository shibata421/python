#!/usr/bin/python3
def mdc(numeros):
    menor_numero = min(numeros)

    for num in range(menor_numero, 0, -1):
        restos = map(lambda n: n % num, numeros)
        if sum(restos) == 0:
            return num


if __name__ == "__main__":
    print(mdc((21, 7)))  # 7
    print(mdc((125, 40)))  # 5
    print(mdc((9, 564, 66, 3)))  # 3
    print(mdc((55, 22)))  # 11
    print(mdc((15, 150)))  # 15
    print(mdc((7, 9)))  # 1
