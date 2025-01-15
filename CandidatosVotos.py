#Calcular a quantidade de votos de 3 candidatos

v1=int(input("Quantidade de votos do candidato 1:"))
v2=int(input("Quantidade de votos do candidato 2:"))
v3=int(input("Quantidade de votos do candidato 3:"))

t=v1+v2+v3
print("No total há",t,"votos")

#calcular a percentagem de cada voto

pv1=v1/t*100
pv2=v2/t*100
pv3=v3/t*100

print("percentagem do voto 1:",pv1)
print("percentagem do voto 2:",pv2)
print("percentagem do voto 3:",pv3)

#calcular quem ganhou e se foi com maioria absoluta

if v2>v1 and v1>v3:
    print("Candidato 1 ganhou")
if v2>v1 and v2>v3:
    print("Candidato 2 ganhou")
if v3>v1 and v3>v2:
    print("Candidato 3 ganhou")

if pv1>50 or pv2>50 or pv3>50:
    print("com maioria absoluta")
else:
    print("sem maioria absoluta")
