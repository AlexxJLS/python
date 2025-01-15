dicionario = {'nome':"",'media':"",'situacao':""}


nome = input("Insira o nome")
media = int(input("Insira a média"))
numero_situacao = int(input("Insira 1 se aprovado, 2 se reprovado"))
if numero_situacao == 1:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

dicionario["nome"] = nome
dicionario["media"] = media
dicionario["situacao"] = situacao

print(dicionario)