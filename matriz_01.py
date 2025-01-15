"""Crie uma matriz 2D de tamanho 3x3 e preencha-a com valores inteiros aleatórios."""
import random,numpy as np

def Preencher(matriz):
    for l in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
            matriz[l,c] = random.randint(0,100)
    return matriz

def main():
    FORMA = (3,3)
    matriz = np.zeros(FORMA,'i')
    print(Preencher(matriz))

if __name__ == "__main__":
    main()