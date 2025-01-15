musicas=int(input("Insira o número de musicas do album:"))
duração_total=0

while musicas>0:
    segundos=int(input("Insira a duração da musica:"))
    if segundos==0:
        break
    duração_total=+segundos
    musicas=musicas-1


minutos=duração_total/60
print(minutos)
#INCOMPLETOOOOOOOOOOOO

