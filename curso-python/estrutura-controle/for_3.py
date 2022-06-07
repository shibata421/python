produto = {
    "nome": "Caneta Chic",
    "preco": 14.99,
    "importada": True,
    "estoque": 793
}

for chave in produto:  # pode usar produto.keys()
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, valor)

# as variáveis internas continuam existindo após a executação do laço
print(chave, valor)
