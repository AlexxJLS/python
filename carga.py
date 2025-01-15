#Alexandre José Leandro Santos
pesoatual=0

while True:
    print(f"Peso atual: {pesoatual} Disponibilidade: {10000-pesoatual}")
    print("1.Carregar\n2.Descarregar\n3.Sair\n")
    opçao=input("Escolha uma opção:")
    
    if opçao=="3":
        print("O programa vai encerrar")
        break
    if opçao=="1":
        peso=int(input("Qual o peso a carregar?:"))
        if peso<0:
            print("Valor inválido!")
            continue
        pesoatual=pesoatual+peso
        if pesoatual>10000:
            print("Peso máximo excedido! Peso não aceite")
            pesoatual=pesoatual-peso
    if opçao=="2":
        peso=int(input("Qual o peso a descarregar?:"))
        if peso<0:
            print("Valor inválido!")
            continue
        pesoatual=pesoatual-peso
        if pesoatual<0:
            print("Valor de carga não existe.")
            pesoatual=pesoatual+peso