#!/usr/bin/python3
class ClasseSimples:
    contador = 0

    def __init__(self):
        ClasseSimples.adicionar()

    @classmethod
    def adicionar(cls):
        cls.contador += 1



if __name__ == "__main__":
    list = [ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador) # Esperado 2