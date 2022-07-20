#!/usr/bin/python3
class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


data1 = Data()
print(data1)

data2 = Data(dia=7, ano=2020)
data2.dia=12
print(data2)
