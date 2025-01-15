"""Crie um programa para sortear os números do euro milhões. Devemos sortear 5 números entre 1 e 50 e mais 2 números entre 1 e 12. Os números 
sorteados não se podem repetir. Devemos mostrar os números por ordem crescente."""
import random,numpy as np

def Numeros(numeros):
    contar = 0
    while contar < 5:
        x = random.randint(1,50)
        if x in numeros:
            continue
        else:
            numeros[contar] = x
            contar += 1
    return bubble_sort(numeros)


def Estrelas(estrelas):
    contar = 0
    while contar < 2:
        x = random.randint(1,12)
        if x in estrelas:
            continue
        else:
            estrelas[contar] = x
            contar += 1
            continue
    return bubble_sort(estrelas)

def bubble_sort(arr):
    n = len (arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
    return arr

def main():
    #criar as arrays
    numeros = np.zeros(5,'i')
    estrelas = np.zeros(2,'i')
    print(f"Números:{Numeros(numeros)}")
    print(f"Estrelas:{Estrelas(estrelas)}")

if __name__ == "__main__":
    main()