"""Programa que utiliza uma função para converter um nº de base 2 para base 10"""

def ConverterBase10(valor_binario):
    soma = 0
    expoente = len(valor_binario) - 1
    for posicao in range (len(valor_binario)):
        if valor_binario[posicao] == "1":
            soma = soma + 2 ** expoente
        expoente = expoente - 1   
    return soma


def main():
    base10 = ConverterBase10("1011")
    print(base10)

if __name__ == "__main__":
    main()