import numpy as np

#definir o nº max de elementos
MAX_ITEMS = 1000
#definir o array
vetor = np.empty(MAX_ITEMS,dtype = "i")

#preencher o array
for i in range (1000):
    numeros = i + 1
    vetor[i] = numeros

#mostrar o array
print(vetor)

#mostrar por ordem inversa
for pos in range(MAX_ITEMS - 1,-1,-1):
    print(vetor[pos])