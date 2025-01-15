#pedir ao utilizador uma frase e mostar a frase com a primeira letra de cada palavra em maiuscula


frase=input("Escreva a frase:")

frase=frase.strip()                               #retira os espaços em branco no inicio da string

frase2=frase[0].capitalize()                      #deixar a primeira letra em maiuscula

for i in range(len(frase)-1):    
    if frase [i]==" ":
        frase2=frase2+frase[i+1].upper()
    
    else:
        frase2=frase2+frase[i+1].lower()
print(frase2)