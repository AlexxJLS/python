"""Crie um programa que lê 5 valores para uma array e mais 5 para outro. O programa deve mostrar a soma total de todos os valores de dois arrays."""
import numpy as np

MAX_ITEMS = 5
numeros1 = np.empty(MAX_ITEMS,dtype = "i")
numeros2 = np.empty(MAX_ITEMS,dtype = "i")

#função para ler os dados de um vetor
def ler_dados(numeros):
    """Função que recebe um array e preenche com dados do utilizador"""
    for pos in range(len(numeros)):
        numeros[pos] = int(input("Insira um nº"))

def somar_dados(numeros):
    """Função que recebe um array e devolve a soma total dos valores"""
    soma = 0
    for x in numeros:
        soma = soma + x
        return soma
    
ler_dados(numeros1)
ler_dados(numeros2)
soma = somar_dados(numeros1) + somar_dados(numeros2)

print(soma)