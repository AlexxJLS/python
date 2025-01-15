frase = input("Insira a frase")
frase = frase
frase = frase.strip()
frase += " "
dicionario = {}
palavra = ""
for letra in frase.lower():
    if letra != " ":
        palavra = palavra + letra
    else:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
            palavra =""

print(dicionario)