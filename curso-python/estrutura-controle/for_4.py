from random import randint


def sortear_numero():
    return randint(1, 6)


def eh_par(i):
    return i % 2 == 0


def eh_impar(i):
    return i % 2 == 1


numero_secreto = sortear_numero()
for i in range(1, 7):
    if eh_impar(i):
        continue
    if eh_par(i) and i == numero_secreto:
        print("Acertou o número {}".format(numero_secreto))
        break
else:
    print("Não acertou o número {}".format(numero_secreto))
