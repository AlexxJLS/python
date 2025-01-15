dicionario = {"Portugal":"Lisboa","Espanha":"Madrid","Franca":"Paris","Alemanha":"Berlim","Inglaterra":"Londres"}

for pais,capital in dicionario.items():
    print(f"A capital de {pais} é {dicionario[pais]}")

pais_user = input("Insira o país:")
capital_user = input("Insira a capital:")

dicionario [pais_user] = capital_user

print(dicionario)

pais_procura_capital = input("País a pesquisar?:")

if pais_procura_capital not in dicionario:
    print("País não existe")
else:
    print(f"A capital do país {pais_procura_capital} é {dicionario[pais_procura_capital]}")


capital = input("País a pesquisar?:")

if capital not in dicionario.values():
    print("Essa capital não existe")
else:
    for pais,cap in dicionario.items():
        if cap == capital:
            print(pais)
