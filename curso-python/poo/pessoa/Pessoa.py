class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'nome={self.nome}, idade={self.idade}'

    def is_adulto(self):
        return self.idade >= 18
