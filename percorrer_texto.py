texto=input("Insira o seu nome:")

contar=0
vogais=0

for letra in texto:
    #print(letra)
    if letra==(" "):
        contar=contar+1
    if letra in "aeiouAEIOUáéíóúãõâêîôû":
        vogais=vogais+1
        
print("Tem %d palavras"%(contar+1))
print("Tem %d vogais"%(vogais))