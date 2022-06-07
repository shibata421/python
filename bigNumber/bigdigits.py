from array import array

zero = [" ***** ",
        "*     *",
        "*     *",
        "*     *",
        "*     *",
        "*     *",
        " ***** "]
um   = ["   *   ",
        "  **   ",
        "   *   ",
        "   *   ",
        "   *   ",
        "   *   ",
        "  ***  "]
dois = ["  **** ",
        " *    *",
        " *   * ",
        "    *  ",
        "   *   ",
        "  *    ",
        " ******"]
tres = [" ***** ",
        "*     *",
        "      *",
        "****** ",
        "      *",
        "*     *",
        " ***** "]
quatro = ["*     *",
          "*     *",
          "*     *",
          "*******",
          "      *",
          "      *",
          "      *"]
cinco = ["*******",
         "*      ",
         "*      ",
         "*******",
         "      *",
         "      *",
         "*******"]
seis = [" ***** ",
        "*     *",
        "*      ",
        "****** ",
        "*     *",
        "*     *",
        " ***** "]
sete = ["*******",
        "      *",
        "      *",
        "      *",
        "      *",
        "      *",
        "      *"]
oito = [" ***** ",
        "*     *",
        "*     *",
        " ***** ",
        "*     *",
        "*     *",
        " ***** "]
nove = [" ***** ",
        "*     *",
        "*     *",
        " ******",
        "      *",
        "*     *",
        " ***** "]

def criar_dicionario() :
    dicionario = {}
    digitos = [zero, um, dois, tres, quatro, cinco, seis, sete, oito, nove]
    
    for i in range (0, 10):
        dicionario[str(i)] = digitos[i]
    
    return dicionario

def criar_array_numeros(numero_digitado):
    dicionario = criar_dicionario()
    array_numero = []
    
    for numero in str(numero_digitado):
        array_numero.append(dicionario.get(numero))
    
    return array_numero

def criar_numero_grande(array_numeros):
    linhas = []

    for indice in range (0,7):
        linha = ''
        for numero in array_numeros:
            linha += numero[indice] + "  "
        linhas.append(linha)

    return linhas

def imprimir_numero(linhas):
    for linha in linhas:
        print(linha)

def principal():
    numero = input("Digite um número: ")
    array_numero = criar_array_numeros(numero)
    linhas = criar_numero_grande(array_numero)
    imprimir_numero(linhas)


principal()