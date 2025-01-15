"""O Sr Joaquim tem um restaurante com 6 mesas de 4 lugares cada.
Vamos fazer um programa para:
1. Entrada de Clientes - deve perguntar qual é a mesa e quantas pessoas 
2. Saida de Clientes - deve perguntar qual a mesa
3. Listar Mesas - listar as mesas livres e ocupadas
4. Terminar - deve pedir para confirmar
Versão hacker:
O Sr. Joaquim deve poder inserir o nº de mesas e a lotação de cada mesa
"""
import numpy as np

def Menu():
    print("\nMenu:\n1.Entrada de Clientes\n2.Saida de Clientes\n3.Listar Mesas\n4.Terminar")
    opcao = input("Insira a opção:")
    return opcao


def EntradaClientes(mesas):
    if Nr_Mesas_livres(mesas) == 0:
        print("O restaurante está cheio!")
        return 
    while True:
        #perguntar qual a mesa
        nr_mesa = int(input("Qual a mesa?[1-6]:"))-1
        #verificar se o nº da mesa é valido
        if nr_mesa < 0 or nr_mesa > len(mesas)-1:
            print("Mesa não é válido!")
            continue
        #verificar se a mesa está ocupada
        if mesas[nr_mesa] != 0:
            print("Essa mesa está ocupada")
        else:
            break
        #perguntar quantas pessoas
    while True:
        nr_pessoas = int(input("Quantas pessoas?:"))
        if nr_pessoas <= 0 or nr_pessoas > 4:
            print("Nº de pessoas não é valido")
        else:
             break
    #registar as entradas
    mesas[nr_mesa] = nr_pessoas
    print(f"Pode sentar-se na mesa {nr_mesa+1}!")


def SaidaClientes(mesas):
    while True:
        if Nr_Mesas_livres(mesas) == len(mesas):
            print("O restaurante está vazio!")
            return
        #perguntar a mesa
        nr_mesa = int(input("Qual a mesa?[1-6]:"))-1
        #verificar se o nº da mesa é valido
        if nr_mesa < 0 or nr_mesa > len(mesas)-1:
            print("Mesa não é válido!")
            continue
        #verificar se a mesa está ocupada
        if mesas[nr_mesa] == 0:
            print("Essa mesa não está ocupada!")
        else:
            break
    #registar a saída
    mesas[nr_mesa] = 0
    print("Obrigado pela visita!")


def ListarMesas(mesas):
    soma = 0
    #listar as mesas livres
    for m in range(len(mesas)):
        soma = soma + mesas[m]
        if mesas[m] == 0:
            print(f"A mesa {m + 1} está vazia")
    #listar as mesas ocupadas
    for m in range(len(mesas)):
        if mesas[m] != 0:
            print(f"A mesa {m + 1} está ocupada")
    #listar o nº de clientes 
    print(f"Tem {soma} clientes no restaurante")

def Nr_Mesas_livres(mesas):
    #Função devolve o nº de mesas livres
    contar = 0
    for mesa in mesas:
        if mesa == 0:
            contar += 1
    return contar 

def Main():
    NR_MESAS = 6
    mesas = np.zeros(NR_MESAS,'i')
    #menu
    while True:
        op = Menu()
        
        if op == "1":
            EntradaClientes(mesas)

        elif op == "2":
            SaidaClientes(mesas)
        
        elif op == "3":
            ListarMesas(mesas)
        
        elif op == "4":
            print("O programa vai terminar!")
            break
        else:
            print("Opção não é valida")
        
if __name__ == "__main__":
    Main()