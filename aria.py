# Inicializar a variável para armazenar a soma das temperaturas
soma_temperaturas = 0

# Inicializar a variável para armazenar a maior temperatura
maior_temperatura = float('-inf')

# Loop for para obter as 5 temperaturas
for i in range(5):
    temperatura = float(input("Digite a temperatura: "))
    
    # Adicionar a temperatura à soma total
    soma_temperaturas += temperatura
    
    # Verificar se a temperatura é a maior até agora
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura

# Calcular a média das temperaturas
media_temperaturas = soma_temperaturas / 5

# Exibir a média e a maior temperatura
print("A média das temperaturas é:", media_temperaturas)
print("A maior temperatura é:", maior_temperatura)