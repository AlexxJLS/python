maior_temperatura = float(input("Digite a primeira temperatura: "))
soma_temperaturas = maior_temperatura

i=0

#for i in range(4)
while i<4:
    temperatura = float(input(f"Digite a {i+2}ª temperatura: "))
    i=i+1
    soma_temperaturas += temperatura
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura

media_temperaturas = soma_temperaturas / 5

print(f"A média das temperaturas é {media_temperaturas:.2f} graus Celsius.")
print(f"A maior temperatura é {maior_temperatura:.2f} graus Celsius.")
