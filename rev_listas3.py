palavras=[]
vogais="aeiou"

for x in range(10):
    palavra=input("Palavra:")
    palavras.append(palavra)

#contar nº letras lidas
soma=0
for palavra in palavras:
    soma=soma+len(palavra)

print(f"Foram lidas {soma} letras")

#mostrar as consoantes
for palavra in palavras:
    for letra in palavras:
        if letra not in vogais:
            print(letra)

#mostrar a maior palavra
maior=palavra[0]
for palavra in palavras:
    if len(palavra)>len(maior):
        maior=palavra
print(f"A maior palavra{maior}")

#contar as palavras que começam por a
contar=0
for palavras in palavra:
    if palavra[0] in 'aA':
        contar+=1
print(f"{contar} palavras que começam por a")