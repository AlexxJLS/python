"""Precisamos de um programa para gerir as temperaturas médias mensais de um ano.
O programa dever ler as 12 temperaturas e depois mostrar o mês mais quente e mais frio.
Opcional: calcular e mostrar a temperatura média do ano e quantos meses tiveram temperatura superior à média"""

import numpy as np

meses = np.array(["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"])
MAX_ITEMS = 12

def Ler_dados(temperaturas):   
    for pos in range(MAX_ITEMS):
        temperaturas[pos] = float(input(f"Insira a temperatura do mês de {meses[pos]}:"))

def MaiorMenor(temperaturas):
    maior = temperaturas[0]
    menor = temperaturas[0]
    maior_mes = meses[0]
    menor_mes = meses[0]
    for i in range(1,MAX_ITEMS):
        if maior < temperaturas[i]:
            maior = temperaturas [i]
            maior_mes = meses[i]
        if menor > temperaturas[i]:
            menor = temperaturas[i]
            menor_mes = meses[i]
        
    print(f"A maior temperatura foi {maior}, do mês de {maior_mes}")
    print(f"A menor temperatura foi {menor}, do mês de {menor_mes}")

def Media(temperaturas):
    soma_temp = 0
    for n in range(MAX_ITEMS):
        soma_temp = soma_temp + temperaturas[n]

    media = soma_temp / MAX_ITEMS
    print(f"A média é {media}")

    contar = 0
    for p in range(MAX_ITEMS):
        if temperaturas[p] > media:
            print(f"No mês de {meses[p]}, a temperatura foi maior à média")
            contar = contar + 1
    print(f"No total, {contar} meses tiveram uma temperatura superior à média")

def main():
    temperaturas = np.empty(MAX_ITEMS,"f")
    Ler_dados(temperaturas)
    MaiorMenor(temperaturas)
    Media(temperaturas)

if __name__ == "__main__":
    main()