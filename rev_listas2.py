'''Manipulação de Notas
a) Leia 4 notas e mostre as notas e a média
    1. Calcule a percentagem de positivas e negativas
    2. Mostre a melhor nota'''

notas = [13,20,5,18]

# a)
media=sum(notas)/len(notas)
print(notas)
print(media)

melhor_nota=notas[0]
nr_positivas=0
for nota in notas:
    if nota>=10:
        nr_positivas+=1
    if nota>melhor_nota:
        melhor_nota=nota

p_positivas=nr_positivas/len(notas)*100
p_negativas=100-p_positivas

print(f"A melhor nota foi {melhor_nota}")
print(f"Percentagem de positivas: {p_positivas}%")
print(f"Percentagem de negativas: {p_negativas}%")

