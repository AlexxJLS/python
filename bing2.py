soma_temp = 0
max_temp = float('inf')
min_temp = float('inf')
i = 0
contar_negativas = 0

#for i in range(1,6):
while i < 5:
    temp = float(input(f'Insira a temperatura {i+1}: '))
    soma_temp += temp
    #verificar se é maior temp
    if temp > max_temp:
        max_temp = temp
    #verificar se é a menor temp
    if temp < min_temp:
        min_temp = temp
    #contar se a temperatura é negativa

    i = i + 1

media =soma_temp / 5

print(f'A média das temperaturas é {media}')
print(f'A maior temperatura é {max_temp}')
print(f'A menor temperatura é {min_temp}')
print(f'Temperaturas positivas: {5-contar_negativas} - negativas: {contar_negativas}')