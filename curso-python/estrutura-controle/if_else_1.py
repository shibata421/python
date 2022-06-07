import sys


def nota_invalida():
    print("Nota inválida")
    sys.exit(1)


def avaliar_nota(nota):
    if nota < 0 or nota > 10:
        nota_invalida()
    elif 9.1 <= nota <= 10.0:
        print("A")
    elif 8.1 <= nota <= 9.0:
        print("A-")
    elif 7.1 <= nota <= 8.0:
        print("B")
    elif 6.1 <= nota <= 7.0:
        print("B-")
    elif 5.1 <= nota <= 6.0:
        print("C")
    elif 4.1 <= nota <= 5.0:
        print("C-")
    elif 3.1 <= nota <= 4.0:
        print("D")
    elif 2.1 <= nota <= 3.0:
        print("D-")
    elif 1.1 <= nota <= 2.0:
        print("E")
    else:
        print("E-")


if __name__ == "__main__":
    nota = float(input("Digite uma nota: "))
    avaliar_nota(nota)
