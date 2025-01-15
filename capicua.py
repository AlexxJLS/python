#ler uma palavra e dizer se é uma capicua
texto=input("Insira a sua palavra:")
texto2=""

for i in range(len(texto)-1,-1,-1):
    texto2=texto2+texto[i]
print("Palavra invertida:",texto2)
if texto==texto2:
    print("A palavra é uma capicua!")
else:
    print("A palavra não é uma capicua!")
