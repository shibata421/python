#!/usr/bin/python3
from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

print(sorted(valores))
print(valores)

# com mutabilidade
# valores.sort()
# print(valores)

print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(list(reversed(valores)))

# com mutabilidade
# valores.reverse()
# print(valores)
