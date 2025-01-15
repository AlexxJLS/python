'''Leitura e Impressão de Listas

a) Faça um programa que leia uma lista de 5 números inteiros e os exiba
    1. Mostre a média dos números inseridos com até 2 casas decimais

b) Crie um programa que leia uma lista de 10 números reais e os mostre na ordem inversa
    1. Mostre qual a percentagem de números positivos e negativos'''

# a)
numeros=[]

#for i in range(5):
    #x=int(input("Valor:"))
    #numeros.append(x)

while True:
    numero=input("Insira 5 números separados por espaços em branco:")
    temp=numero.split()
    if len(temp)>=5:
        break

numeros=[int(x) for x in temp]

numeros=numeros[0:6]


soma=sum(numeros)
media=soma/len(numeros)
print(f"Média {media:.2f}")


# b)
notas=[]

for _ in range(10):
    nota=float(input("Nota:"))
    notas.append(nota)

numeros2_inversos=[]
print(notas)

for i in range(len(notas) - 1,-1,-1):
    numeros2_inversos.append(notas[i])

notas=numeros2_inversos
print(notas)

positivos=0
for i in range(len(notas)):
    if notas[i]>=0:
        positivos+=1

p_positivos=positivos/len(notas)*100
p_negativos=100-p_positivos

print(f"Percentagem de positivos:{p_positivos}%\nPercentagem de negativos:{p_negativos}%")