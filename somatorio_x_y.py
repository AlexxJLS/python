#somar todos os números inteiros entre 2 nº indicados pelo utilizador
#ler os números
x=int(input("Insira um número:"))
y=int(input("Insira outro número:"))

#trocar os valores se o primeiro for maior que o segundo
if x>y:
    t=x
    x=y
    y=t

if x==y:
    soma=x
else:
    soma=0


for i in range(x,y):
    soma=soma+i
print(soma)
