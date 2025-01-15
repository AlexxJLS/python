lista_numeros = list(range(5))
print(lista_numeros)

print(type(lista_numeros))

lista_numeros_2 = lista_numeros
print(id(lista_numeros))
print(id(lista_numeros_2))

#copia os elementos
lista_numeros_2 = lista_numeros[:]
lista_numeros_2[0] = 100
print(lista_numeros)
print(lista_numeros_2)

#listar pelas posições
for i in range(len(lista_numeros)):
    print(lista_numeros[i])

#adicionar elementos
lista_numeros.append(1366)
print(lista_numeros)

#juntar duas listas
lista_numeros.insert(0,"Viseu")
print(lista_numeros)

#juntar duas listas com +
frutas = ["maçã","laranjeira"]
arvores = ["macieira","laranjeira"]
juntar = frutas + arvores
print(juntar)
frutas[0] = "banana"
print(juntar)

arvore = arvores.pop(1)
print(arvore)

print(lista_numeros)
del lista_numeros[1:4] #remove os elementos das posições 1,2,3
print(lista_numeros)

#remove todos os elementos
lista_numeros = []
arvores.clear()