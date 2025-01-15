#calcular positivas ou negativas

dados=input("Insira o número de alunos")
if dados.isdigit()==False:
    print("Dados Inválidos, insira um número inteiro de 0 a 20!!!")
else:
    alunos=int(dados)
    positiva=0
    negativa=0
    for i in range(alunos):
        nota=int(input("Insira a nota de 0 a 20:"))
        if nota<0 or nota>20:
            print("Dados invalidos")
            alunos=alunos+1
        elif nota>9:
            positiva=positiva+1
        else:
            negativa=negativa+1
    print("Número de positivas:",positiva)
    print("Número de negativas:",negativa)







        
