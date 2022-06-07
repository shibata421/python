from random import randint

def inserir_int(mensagem, minimum, default = None):
    entrada = input(mensagem)

    if entrada == "":
        print("Será utilizado o valor default")
        return default
    
    if (int(entrada) < minimum):
        print("Entrada inválida. Será usado o valor mínimo")
        return minimum
    
    return int(entrada)

rows = inserir_int("Rows: ", 0)
columns = inserir_int("Columns: ", 0)
mininum = inserir_int("Minimum: ", -1000000000000, 0)
maximum = inserir_int("Maximum: ", -1000000000000, 1000)

for i in range(0, rows):
    linha = ""
    for j in range(0, columns):
        numero_randomico = str(randint(mininum, maximum)).rjust(7, " ")
        linha += numero_randomico
    print(linha)