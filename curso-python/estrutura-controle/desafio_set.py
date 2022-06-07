PALAVRAS_PROIBIDAS = {"futebol", "religião", "política"}
textos = [
    "João gosta de futebol e política",
    "A praia foi divertida"
]

if __name__ == "__main__":
    for texto in textos:
        palavras_texto = set(texto.lower().split())
        intersecao = PALAVRAS_PROIBIDAS.intersection(palavras_texto)

        if intersecao:
            print(f"O texto é proibido por conter {intersecao}")
        else:
            print(f"O texto é válido: {texto}")
