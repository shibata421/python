#!/usr/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt_BR.UTF-8')

meses_com_31_dias = filter(lambda m: m[0] == 31, zip(mdays, month_name))
meses = map(lambda m: m[1], meses_com_31_dias)
frase = reduce(lambda acc, m: acc + f'\n- {m}', meses, 'Meses com 31 dias:')
print(frase)
