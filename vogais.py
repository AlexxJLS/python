"""
Crie uma função que conte o número de vogais em uma string
"""

import sys

#percorrer pela posição
#def vogais(palavra):
    #n_vogais = 0
    #for i in range(len(palavra)):
        #if palavra[i] in "AEIOUaeiouÃÕãõÁÉÍÚÓáéíóúÀà":
            #n_vogais = n_vogais +1
    #print(f"Existem {n_vogais} vogais na palavra {palavra}")


def vogais(palavra):
    contar = 0
    
    for letra in palavra:
        if letra in "AEIOUaeiouÃÕãõÁÉÍÚÓáéíóúÀà":
            contar = contar + 1
    
    print(f"Existem {contar} vogais na palavra {palavra}")


def main():
    if len(sys.argv) != 2:
        palavra_inserida = input("Insira a palavra:")
    else:
        palavra_inserida = sys.argv[1]
    
    vogais(palavra_inserida)

if __name__ == "__main__":
    main()