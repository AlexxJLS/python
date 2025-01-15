#Alexandre José Leandro Santos
def Soma(numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]
    return soma


def Longa(palavras):
    palavra_longa = palavras[0]
    for i in range(len(palavras)):
        if len(palavra_longa) < len(palavras[i]):
            palavra_longa = palavras[i]
    return palavra_longa


def main():
    numeros = (2,23,76,2,54,2)
    print(Soma(numeros))
    
    palavras = ('arroz','joao','martelo','corrente')
    print(Longa(palavras))

if __name__ == "__main__":
    main()