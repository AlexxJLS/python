"""Fazer um programa que lê 10 números e mostra o maior e o menor e as suas posições"""
import numpy as np

MAX_VETOR = 10
maior = 0

#criar um vetor de floats
vetor = np.empty(MAX_VETOR,dtype ="f")

#ler os valores para o vetor
for i in range(len(vetor)):
    vetor[i] = float(input(f"Introduza um número para a posição {i+1}:"))

#econtrar o maior
#começamos por assumir que o maior é o primeiro
pos_maior = 0
maior = vetor[0]
#vamos percorrer o vetor e procurar o maior
for p in range(MAX_VETOR):
    if  vetor[p] > maior:
        maior = vetor[p]
        pos_maior = p
print(f"O maior é {maior} e está na posição {pos_maior+1}")

#vamos percorrer o vetor e procurar o menor
pos_menor = 0
menor = vetor[0]
for p in range(MAX_VETOR):
    if  vetor[p] < menor:
        menor = vetor[p]
        pos_menor = p
print(f"O maior é {menor} e está na posição {pos_menor+1}")

