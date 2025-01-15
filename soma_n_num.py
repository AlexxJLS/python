#pretendemos somar n valores inseridos pelo utilizador
n=int(input("Quantos valores pretende inserir: "))

soma=0
for i in range(n):
    x=int(input("Introduza um valor:"))
    if i==0:
        maior=x
    elif x>maior:
        maior=x
    soma=soma+x

print("O maior número inserido é:",maior)
print("Soma:",soma)
print("Média: %.2f"%(soma/n))


