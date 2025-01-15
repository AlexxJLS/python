"""Fazer um programa para gerir os contactos de uma agenda. Deve permitir adicionar nome e telefone de cada contacto. Deve permitir listar todos e 
pesquisar por um nome. Deve permitir Alterar o telefone de um nome."""

import numpy as np

def Menu():
    print("\nMenu:\n1. Adicionar contacto\n2. Listar\n3. Pesquisar\n4. Editar\n5. Terminar\n")
    op = input("Insira a opção:")
    return op

#função para adicionar novo contacto e devolve o nr de contactos
def AdicionarNovo(contactos,nr_contactos):
    nome = input("Nome do novo contacto:")
    numero = input("Número do novo contacto:")
    #verifi
    #guardar na matriz
    contactos[nr_contactos,0] = nome
    contactos[nr_contactos,1] = numero
    nr_contactos += 1
    #devolve o nr de contactos
    return nr_contactos


def NomeRepetido(contactos,nr_contactos,nome):
    for i in range(nr_contactos):
        return True
    return False

def AdicionarNovo_V2(contactos, nr_contactos):
    if nr_contactos == contactos.shape[0]:
        print("A agenda está cheia")
        return
    nome = input("Nome do novo contacto:")
    if NomeRepetido(contactos,nr_contactos,nome):
        print("Nome já existe na agenda!")
        return
    numero = input("Número do novo contacto:")
    if nr_contactos == 0:
        #guardar na matriz
        contactos[nr_contactos,0] = nome
        contactos[nr_contactos,1] = numero
        nr_contactos += 1
        #devolve o nr de contactos
        return nr_contactos
    else:
        for linha in range(nr_contactos):
            if nome < contactos[linha,0]:
                #copiar  os restantes uma posição para a frente
                for posicao in range(nr_contactos,linha,-1):
                    contactos[posicao,0] = contactos[posicao - 1,0]
                    contactos[posicao,1] = contactos[posicao - 1,1]
                contactos[linha,0] = nome
                contactos[linha,1] = numero
                nr_contactos += 1
                return nr_contactos
        #inserir no final
        contactos[nr_contactos,0] = nome
        contactos[nr_contactos,1] = numero
        nr_contactos += 1
        #devolve o nr de contactos
        return nr_contactos


def Listar(contactos,nr_contactos):
    for linha in range(nr_contactos):
        print(f"Nome:{contactos[linha,0]} - Telefone:{contactos[linha,1]}")

#mostra o nº de um ou vários contactos com base em parte do nome
def Pesquisar(contactos,nr_contactos):
    nome = input("Nome a pesquisar:")
    encontrei= False
    for i in range(nr_contactos):
        if nome in contactos[i,0]:
            print(f"Nome:{contactos[i,0]} - Telefone:{contactos[i,1]}")
            encontrei = True
    if encontrei == False:
        print(f"Não existe nenhum contacto com o nome {nome}")
            

def Editar(contactos,nr_contactos):
    nome = input("Nome a pesquisar:")
    encontrei= False
    for i in range(nr_contactos):
        if nome in contactos[i,0]:
            print(f"Nome:{contactos[i,0]} - Telefone:{contactos[i,1]}")
            encontrei = True
            op = input("Quer alterar [s ou n]?:")
            if op == "s":
                novo_nome = input("Nome do novo contacto ou deixe em branco:")
                novo_contacto = input("Número do novo contacto ou deixe em branco:")
                if novo_nome != "":
                    contactos[i,0] = novo_nome
                if novo_contacto != "":
                    contactos[i,1] = novo_contacto
                print("Contacto atualizado com sucesso")
    if encontrei == False:
        print(f"Não existe nenhum contacto com o nome {nome}")


def main():
    #vai ter 100 linhas e 2 colunas
    FORMA = (100,2)
    contactos = np.zeros(FORMA,'U50') #strings com 50 letras cada no máximo
    nr_contactos = 0
    while True:
        op = Menu()
        if op == "1":
            nr_contactos = AdicionarNovo_V2(contactos,nr_contactos)
        elif op == "2":
            Listar(contactos,nr_contactos)
        elif op == "3": 
            Pesquisar(contactos,nr_contactos)
        elif op == "4":
            Editar(contactos,nr_contactos)
        elif op == "5":
            break
        else:
            print("Opção inválida")
        
            
if __name__ == "__main__":
    main()