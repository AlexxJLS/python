print("O jogo começou!")

import random
numero_secreto=int(random.random()*10+1)

while True:
    tentativas=int(input("Número de tentativas de (1 a 5):"))
    if tentativas<1 or tentativas>5:
        print("Número inválido. Introduza um nº de 1 a 5")
        continue
    else:
        break


while tentativas>0:
    print("Tem %d tentativas"%tentativas)
    numero_adivinha=int(input("Adivinhe o número entre 1 e 10:"))
    if numero_adivinha>10 or numero_adivinha<0:
        print("O número é invalido")
        continue
    if numero_adivinha==numero_secreto:
        print("Acertou!!! Parabéns!!!")
        break
    elif numero_adivinha<numero_secreto:
            print("O número secreto é maior que %d" %numero_adivinha)
            tentativas=tentativas-1
    else:
            print("O número secreto é menor que %d"%numero_adivinha)
            tentativas=tentativas-1
else:
     print("Ficou sem tentativas,o número secreto era %d"%numero_secreto)



