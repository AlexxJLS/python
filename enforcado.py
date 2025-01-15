#Jogo do enforcado
 
palavra = input("Insira a palavra:")

tentativas=7

palavra_j = "_"*len(palavra)

while tentativas > 0:                              
    letra = input("Letra:")                          
    temp = ""
    acertou = False
    for i in range(len(palavra)):                  
        if letra == palavra[i]:
            temp += letra
            acertou = True
        else:
            temp += palavra_j[i]
    
    palavra_j = temp 
    
    if acertou == False:
        tentativas -= 1

    if palavra == palavra_j:
        print("Acetou na palavra: {palavra}")
        break
    
    
    print(palavra_j)
    print(f"Tentativas restantes {tentativas}")

    






