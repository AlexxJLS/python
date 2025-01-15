dados=input("Insira a sua Idade (De 0 a 120):")
if dados.isdigit()==False:
    print("Tem de indicar a sua idade em valores numéricos")
else:
    idade=int(dados)
    if idade<0 or idade>120:
        print("Idade inserida não é válida")
    elif idade<=11:
        print("Fase da Infância")
    elif idade<=20:
        print("Fase da Adolescência")
    elif idade<=74:
        print("Fase Adulta")
    else:
        print("Fase da Velhice")
    
