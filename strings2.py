from string import punctuation             #importar o codigo de uma libraria

frase=input("Escreva a sua frase:")

for i in range(len(frase)-1):
    if frase[i].isalpha():                 #testa se é texto
        print("alfabeto")
    if frase[i].isdigit():                 #testa se é números
        print("Número")
    if frase[i].isspace():                 #testa se ha espaços
        print("espaço")
    if frase[i] in punctuation:            #testar se há pontuação 
        print("pontuação")