"""Crie um programa que lê 5 valores para uma array e mais 5 para outro. O programa deve mostrar a soma total de todos os valores de dois arrays."""
import numpy as np

MAX_ITEMS = 5
numeros1 = np.empty(MAX_ITEMS,dtype = "i")
numeros2 = np.empty(MAX_ITEMS,dtype = "i")

#ler os dados para os vetores
soma = 0
for i in range(MAX_ITEMS):
    numeros1[i] = int(input("Insira um nº:"))
    soma = soma + numeros1[i]

for n in range(MAX_ITEMS):
    numeros2[n] = int(input("Insira um nº:"))
    soma = soma + numeros2[n]

print(soma)