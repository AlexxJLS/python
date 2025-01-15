"""Programa para gerir um moedeiro de uma máquina de vending. 
O programa deve permitir inserir os stock de moedas existentes
Depois de perguntar o valor a pagar e o dinheiro entrege o programa deve calcular o troco e as moedas que perfazem o valor do troco.
Podem não ser possível devolver o troco por falta de moedas"""

import numpy as np

moedeiro = np.array([[0.01,0],[0.02,0],[0.05,0],[0.1,0],[0.2,0],[0.5,0],[1,0],[2,0]])

#perguntar ao utilizador quantas moedas de cada tipo existem no moedeiro
for i in range(moedeiro.shape[0]):
    stock_moedas = int(input(f"Quantas moedas de {moedeiro[i,0]:.2f}?: "))
    moedeiro[i,1] = stock_moedas

#perguntar ao utilizador total a pagar
valor_pagar = float(input("Qual o valor a apagar?:"))

#perguntar dinheiro inserido
dinheiro_inserido = float(input("Insira o dinheiro:"))
    
#calcular o troco
troco = dinheiro_inserido - valor_pagar

if troco > 0:
    print(f"Vai receber {troco:.2f}")

#dar o troco
while troco > 0:
    troco_ant = troco
    for i in range(moedeiro.share[0],-1,-1):
        if moedeiro[i,0] <= troco and moedeiro[i,1] > 0:
            moedeiro[i,1] -= 1
            print(f"Recebeu uma moeda de {moedeiro[i,0]}")
            troco -= moedeiro[i,0]
            break
    if troco_ant == troco:
        print("Não temos + moedas")
        break