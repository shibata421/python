#!/usr/bin/python3
from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

idades = map(lambda p: p['idade'], pessoas)
menores = filter(lambda i: i < 18, idades)
soma_idades = reduce(lambda soma, idade: soma + idade, menores, 0)
print(soma_idades)
