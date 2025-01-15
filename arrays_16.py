"""Implemente uma fila para 10 elementos, simulando uma fila de um restaurante com drive in.
O programa deve disponibilizar as seguintes opções:
1. Entrada na Fila
2. Saída da Fila
3. Estado da Fila
4. Terminar
"""

import numpy as np

def Menu():
    #mostra e lê do utilizador a ooção do menu
    #devolve a opção se for válida
    while True:
        print("\nMenu:\n1.Carro que entrou\n2.Carro que saiu\n3.Mostrar o estado da fila\n4.Terminar\n")
        op = int(input(":"))
        if op < 1 or op > 4:
            print("Opção não é valida!")
        else:
            return op

def Entrada(fila,nr_elementos):   
    #recebe a fila e adiciona a nova matricula à fila 
    #devolver o nr de elementos da fila
    #deve verificar se a fila está cheia
    if IsFull(fila,nr_elementos) == True:
        print("A fila está cheia")
        return nr_elementos
    matricula = input("Qual a matricula:")
    fila[nr_elementos] = matricula
    nr_elementos += 1
    return nr_elementos

def Saida(fila, nr_elementos):
    #recebe a fila e retira uma matrícula da fila
    #deve verificar se a fila está vazia
    if nr_elementos == 0:
        print("A fila está vazia")
        return nr_elementos
    #retirar o elemento da posição 0
    elemento_retirado = fila[0]
    print(f"Sai o {elemento_retirado}")
    for i in range(nr_elementos-1):
        fila[i] = fila[i+1]
    #reduzir o nº de elementos
    nr_elementos -= 1
    #devolver o nr de elementos da fila
    return nr_elementos


def MostrarEstado(fila,nr_elementos):
    #mostrar o estado da fila por ordem de chegada (FIFO)
    #se a fila estiver vazia mostrar uma mensagem
    if nr_elementos == 0:
        print("Fila vazia")
        return
    for i in range(nr_elementos):
        print(fila[i])

def IsFull(fila,nr_elementos):
    if len(fila) == nr_elementos:
        return True
    return False

def main():
    NR_MAX_CARROS = 10
    fila = np.empty(NR_MAX_CARROS,'U10')    #a fila com os elementos
    nr_elementos = 0        #nº de elementos na fila
    #ler opção do menu
    #executar a opção do menu
    while True:
        op = Menu()
        if op == 1:
            nr_elementos = Entrada(fila,nr_elementos)
        elif op == 2:
            nr_elementos = Saida(fila,nr_elementos)
        elif op == 3:
            MostrarEstado(fila,nr_elementos)
        else:
            break
        
if __name__ == "__main__":
    main()
