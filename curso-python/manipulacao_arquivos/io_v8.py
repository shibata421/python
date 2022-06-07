import csv

with open('desafio-ibge.csv') as entrada:
    for indice, linha in enumerate(csv.reader(entrada)):
        if indice == 4:
            print(linha)
