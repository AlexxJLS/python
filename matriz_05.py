import numpy as np


def Diagonal(matriz):
    for i in range(matriz.shape[0]):
        matriz[i,i] = 1

def main():
    FORMA = (4,4)
    matriz = np.zeros(FORMA,'i')
    Diagonal(matriz)
    print(matriz)

if __name__ == "__main__":
    main()