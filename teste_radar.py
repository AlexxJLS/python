P1=float(input("Valor dos minutos no ponto 1:"))
P2=float(input("Valor dos minutos no ponto 2:"))
D=float(input("Distância entre os dois pontos:"))

tempo_minutos=P2-P1
tempo_segundos=tempo_minutos*60
velocidade_media=D/tempo_segundos

print(velocidade_media)
