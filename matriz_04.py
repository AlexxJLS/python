"""Transposição de Matriz: Crie uma função que retorne a matriz transposta de uma matriz dada."""
import numpy as np

def Transposta(matriz):
    FORMA = (matriz.shape[1],matriz.shape[0])
    matriz_transposta = np.zeros(FORMA,'i')
    for l in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
            matriz_transposta [c,l] = matriz[l,c]
    return matriz_transposta

def main():
    matriz = np.array([[1,2],[3,4],[5,6]])
    matriz_trasnsposta = Transposta(matriz)
    print(matriz_trasnsposta)

if __name__ == "__main__":
    main()