import numpy as np

MAX_VETOR = 10

#criar array
vetor = np.empty(MAX_VETOR)

#ler os valores
for i in range(len(vetor)):
    vetor[i] = int(input("Insira os nº:"))

print(vetor)

#mostrar os valores por ordem inversa
for i in range(MAX_VETOR - 1,-1,-1):
    print(vetor[i])