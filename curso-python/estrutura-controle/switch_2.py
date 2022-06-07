def get_tipo_dia(dia):
    if dia in range(2, 7):
        return "Dia da semana"

    if dia in {1, 7}:
        return "Fim de semana"

    return "** inválido **"


if __name__ == "__main__":
    for dia in range(1, 8):
        print(get_tipo_dia(dia))
