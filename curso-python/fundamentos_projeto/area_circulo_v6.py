#! python
from math import pi

raio = float(input("Digite o raio do círculo: "))
area = pi * raio ** 2

print(f"A área do círculo é {area}")

print("Nome do módulo", __name__)  # __main__
print("Nome do pacote", __package__)  # None
