#!/usr/bin/python3
lista_1 = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

print('Menores de idade')
menores = filter(lambda p: p['idade'] < 18, lista_1)
[print(menor) for menor in menores]

print('Nomes grandes')
nomes_grandes = filter(lambda p: len(p['nome']) > 6, lista_1)
[print(nome) for nome in nomes_grandes]
