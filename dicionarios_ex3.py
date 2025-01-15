import random
import numpy as np

def LançarDados(array):
    soma = 0
    for i in range(6):
        dado = random.randint(1,6)
        print(f"{i+1}º dado:{dado}")
        soma += dado
        array[i] = dado
    print("Acabaram as chances!")
    return soma

#ordenação bolha
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t

def main():
    print("Vai começar o jogo!")
    
    input("Jogador 1, prima Enter")
    dados_1 = np.zeros(6,'i')
    total1 = LançarDados(dados_1)

    input("Jogador 2, prima Enter")
    dados_2 = np.zeros(6,'i')
    total2 = LançarDados(dados_2)

    input("Jogador 3, prima Enter")
    dados_3 = np.zeros(6,'i')
    total3 = LançarDados(dados_3)

    input("Jogador 4, prima Enter")
    dados_4 = np.zeros(6,'i')
    total4 = LançarDados(dados_4)

    dicionario = {'Jogador1':dados_1,'Jogador2':dados_2,'Jogador3':dados_3,'Jogador4':dados_4}

    arraytotal = np.array([total1,total2,total3,total4])
    #copia
    arraytotal2 = np.array([total1,total2,total3,total4])
    bubble_sort(arraytotal2)

    totalvencedor = arraytotal2[0]
    for i in range(len(arraytotal)):
        if arraytotal[i] == totalvencedor:
            vencedor = i+1
    
    print(dicionario)
    print(f"O jogador {vencedor} foi o vencedor, com um total de {totalvencedor} pontos!")

    

if __name__ == "__main__":
    main()