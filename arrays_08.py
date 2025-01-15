"""Crie um programa que lê 10 valores e mostre quais desses valores são repetidos e quantas vezes se repetem"""
import numpy as np

MAX_ITENS = 10

numeros = np.empty(MAX_ITENS)

for i in range(MAX_ITENS):
    numeros[i] = int(input("Insira o número:"))

for x in numeros:
    contar = 0
    for y in numeros:
        if x == y:
            contar += 1
        if contar > 1:
            print(f"O nº {x} repete-se{contar} vezes.")
        