"""Implemente uma função que remove todas os números duplicados de um array.
Por exemplo, transformar [1, 2, 2, 3, 3, 3, 4] em [1, 2, 3, 4, 0, 0, 0]."""
import numpy as np

def Remove_Duplicados(numeros):
    #array temporária 
    temp = np.zeros(len(numeros))
    pos = 0
    for i in range(len(numeros)):
        #se o numero não existir em temp, adicionar
        if numeros[i] in temp:
            continue
        else:
            temp[pos] = numeros[i]
            pos += 1
    numeros = temp
    return numeros
    
def main():
    numeros = np.array([1,2,2,3,3,3,4])
    resultado = Remove_Duplicados(numeros)
    print(resultado)

if __name__ == "__main__":
    main()
