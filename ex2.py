n1 = 0
n2 = 1

n_vezes = int(input("Insira o número de vezes:"))
while n_vezes > 0:
    soma = n1 + n2
    print("%d+%d=%d"%(n1,n2,soma))
    n2 = n1
    n1 = soma
    n_vezes = n_vezes - 1

