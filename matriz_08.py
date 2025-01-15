"""Substituição de Elementos: Dada uma matriz, substitua todos os elementos negativos por zero."""
import numpy as np

def NegativosZero(matriz):
    for l in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
            if matriz[l,c] < 0:
                matriz[l,c] = 0

def main():
    matriz = np.array([[1,2,3,-7],[1,-2,33,0],[1,4,-3,0]])
    NegativosZero(matriz)
    print(matriz)

if __name__ == "__main__":
    main()