palavra_passe = input("Insira a sua senha:")

avaliação_números=0
avaliação_minusculas=0
avaliação_maiusculas=0
avaliação_especiais=0



if len(palavra_passe)<7:
    print("Fraca")
else:
    for letra in palavra_passe:
        if letra in "0123456789":
            avaliação_números=1
        if letra in "#&£$@%!?;:.-_=+*<>\\/^~{}()[]":
            avaliação_especiais=1
        if ord(letra)>=97 and ord(letra)<=122:
            avaliação_minusculas=1
        if ord(letra)>=65 and ord(letra)<=90:
            avaliação_maiusculas=1
    avaliação=avaliação_maiusculas+avaliação_especiais+avaliação_minusculas+avaliação_números

    if avaliação==1:
        print("Fraca")
    elif avaliação<=3:
        print("Média")
    else:
        print("Forte")

        
    
