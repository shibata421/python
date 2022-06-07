#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import cmath
import math
import sys


def get_float(msg, allow_zero):
    number = None
    while number is None:
        try:
            number = float(input(msg))
            if not allow_zero and float_sao_iguais(number, 0.0):
                print("zero is not allowed")
                number = None
        except ValueError as err:
            print(err)
    return number

def float_sao_iguais(num1, num2):
    return abs(num1) - abs(num2) < sys.float_info.epsilon

def float_eh_zero(num):
    return float_sao_iguais(num, 0)

def imprimir_resultado(a, b, c, x1, x2):
    redacao = "{0}x\N{SUPERSCRIPT TWO}".format(a)

    if not float_eh_zero(b):
        redacao += " + {0}x".format(b) 
    
    if not float_eh_zero(c):
        redacao += " + {0}".format(c) 
    
    redacao += " = 0 \N{RIGHTWARDS ARROW} x = {0}".format(x1)

    if x2 is not None:
        redacao += " or x = {0}".format(x2)
    
    print(redacao)


print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

x1 = None
x2 = None
delta = (b ** 2) - (4 * a * c)
if delta == 0:
    x1 = -(b / (2 * a))
else:
    if delta > 0:
        raiz_delta = math.sqrt(delta)
    else: # discriminant < 0
        raiz_delta = cmath.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)

imprimir_resultado(a, b, c, x1, x2)
