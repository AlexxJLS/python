#Alexandre José Leandro Santos

import numpy as np

def MediaPares(numeros):
    soma = 0
    contar = 0
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            soma += numeros[i]
            contar += 1
    media_pares = soma / contar
    return media_pares


def main():
    nr_elementos = int(input("Quantos números irá inserir?:"))
    array = np.zeros(nr_elementos,'i')
    for i in range(nr_elementos):
        n = int(input(f"Insira o {i+1}º nº:"))
        array[i] = n
    
    numeros = tuple(array)

    media_pares = MediaPares(numeros)
    print(media_pares)


if __name__ == "__main__":
    main()