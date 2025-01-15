"""Soma de Matrizes: Dadas duas matrizes 2D, escreva um programa para calcular a soma delas."""

import numpy as np,random

def Soma(arr1,arr2,arr3):
    for l in range(arr3.shape[0]):
        for c in range(arr3.shape[1]):
            arr3[l,c] = arr1[l,c] + arr2[l,c]
    return arr3

def Aleatorio(arr):
    for l in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            arr[l,c] = random.randint(1,10)
    return arr

def main():
    FORMA = (2,2)
    array1 = np.zeros(FORMA,'i')
    array2 = np.zeros(FORMA,'i')
    array3 = np.zeros(FORMA,'i')
    
    arr_al_1 = Aleatorio(array1)
    arr_al_2 = Aleatorio(array2)
    
    resultado = Soma(arr_al_1,arr_al_2,array3)
    print(resultado)

if __name__ == "__main__":
    main()