"""Um programa para ler do utilizador as temperaturas mensais de 3 cidades. O programa deve mostrar a temperatura mais elevada.
Hakcer:
    Calcular a média das temperaturas por cidade
    Calcular a média das temperaturas por mês
    Mostrar a cidade com a temperatura média mais elevada
    Mostrar o mês com a temperatura média mais elevada"""

import numpy as np

#declarar um array de 3 linhas e 12 colunas
MAX_ITEMS = (3,12)
temperaturas = np.empty(MAX_ITEMS)
cidades = np.array(["Viseu","Coimbra","Lisboa"])

#ler as temperaturas
#ciclo para percorrer as linhas(cidades)
for linha in range(temperaturas.shape[0]):
    #ciclo para as colunas
    for coluna in range(temperaturas.shape[1]):
        temp = float(input(f"Introduza a temperatura para a cidade {cidades[linha]} correspondente ao mês {coluna + 1}:"))
        #guardar no array
        temperaturas[linha,coluna] = temp


#procurar a temperatura mais elevada
maior_temperatura = temperaturas[0,0]
#percorrer o array
for linha in range(temperaturas.shape[0]):
    for coluna in range(temperaturas.shape[1]):
        if temperaturas[linha,coluna] > maior_temperatura:
            maior_temperatura = temperaturas[linha,coluna]
print(f"A maior temperatura foi {maior_temperatura}")


#calcular a média das temperaturas por cidade
for linha in range(temperaturas.shape[0]):
    soma = 0
    for coluna in range(temperaturas.shape[1]):
        soma += temperaturas[linha,coluna]
    media = soma / temperaturas.shape[1]
    if linha == 0 or media > maior_media:
        maior_media = media
        cidade = linha
    #elif media > maior_media:
        #maior_media = media
        #cidade = linha
    print(f"A média da temperatura da cidade {cidades[linha]} foi {media:.1f}")
#mostrar a cidade com a temperatura média mais elevada
print(f"A cidade com temperatura média mais elevada foi {cidades[cidade]}")


#calcular a média das temperaturas por mês
for coluna in range(temperaturas.shape[1]):
    soma = 0
    for linha in range(temperaturas.shape[0]):
        soma += temperaturas[linha,coluna]
    media = soma / temperaturas.shape [0]
    if coluna == 0 or media > maior_media:
        maior_media = media
        mes = coluna
    print(f"A média da temperatura do mes {coluna + 1} foi {media:.1f}")
#mostrar o mês com a temperatura média mais elevada
print(f"O mês com temperatura média mais elevada foi {mes + 1}")
