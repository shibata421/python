#!/usr/bin/python3
from app.utils.gerador import novo_nome
from app.negocio import nome_existe
from app.negocio.backend import add_nome

if __name__ == "__main__":
    while True:
        nome = novo_nome()
        if not nome_existe(nome):
            add_nome(nome)
            break

    print(f'Criando novo nome de testes: "{nome}"')
    