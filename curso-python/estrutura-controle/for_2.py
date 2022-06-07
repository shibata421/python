palavra = "paralelepípedo"

for letra in palavra:
    print(letra, end=",")

print()

aprovados = ["Rafaela", "Pedro", "Renato", "Maria"]
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)
