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

import sys
import xml.sax.saxutils

def main():
    (maxwidth, format) = process_options()

    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
            break
    print_end()

def process_options():
    if (sys.argv[1] in ("-h", "--help")):
        print("usage:")
        print("csv2html.py [maxwidth=int] [format=str] <infile.csv> outfile.html")
        print()
        print("maxwidth é uma integer opcional; se esfecificado, configura o número máximo de caracteres que podem entrar no campo da string, "
        "do contrário, o padrão de 100 é usado.")
        print()
        print("format é o formatação usada para números; se não especificado, o padrão é .0f")
        return

    dicionario = {
        "maxwidth": 100,
        "format": ".0f"
    }

    for arguments in sys.argv:
        params = arguments.split("=")
        if len(params) > 1:
            dicionario[params[0]] = params[1]

    maxwidth = dicionario.get("maxwidth")
    format = dicionario.get("format")
    
    return (maxwidth, format)

def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                
                if len(field) <= maxwidth:
                    field = escape_html(field)
                else:
                    field = "{0} ...".format(escape_html(field[:maxwidth]))

                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for caractere in line:
        if caractere in "\"'":
            if quote is None: # start of quoted string
                quote = caractere
            elif quote == caractere:  # end of quoted string
                quote = None
            else:
                field += caractere    # other quote inside quoted string
            continue
        if quote is None and caractere == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += caractere        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def escape_html(text):
    return xml.sax.saxutils.escape(text)


def print_end():
    print("</table>")


main()
