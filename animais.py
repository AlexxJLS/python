animais = {
    ('cão','pitbull'):{'idade':5,'dono':'Joaquim'},
    ('gato','siames'):{'idade':2,'dono':'Carla'},
    ('cão','cão de água'):{'idade':3,'dono':'Joaquim'},
    ('cobra','não sei'):{'idade':1,'dono':'João'},
    ('cão','bulldog'):{'idade':3,'dono':'Maria'},
    }

#listar os animais do joaquim
for chave,valor in animais.items():
    if valor['dono'] == 'Joaquim':
        print(f"Especie: {chave[0]} Raça: {chave[1]} Idade: {valor['idade']}")

#listar quantos animais há por cada especie
contagem ={}
for chave in animais.keys():
    especie = chave[0]
    print(f"{especie=}")  
    #verificar se a especie existe no dicionário
    if especie in contagem:
        contagem[especie] += 1
    else:
        contagem[especie] = 1

print(contagem)

#mostrar o animal mais velho
mais_velho = 0
o_mais_velho = None
for chave,valor in animais.items():
    if valor["idade"] > mais_velho:
        mais_velho = valor["idade"]
        o_mais_velho = chave
print(f"O animal mais velho encontrado foi {o_mais_velho} com {mais_velho} anos")

#media de idades dos animais
soma = 0
for valor in animais.values():
    soma += valor['idade']
media = soma / len(animais)
print(f"A média de idades é {media}")

#mostrar os animais com idade superior à média
for chave,valor in animais.items():
    if valor['idade'] > media:
        print(f"O {chave[0]} de raça {chave[1]} tem idade superior à media. Tem {valor['idade']} anos.")

#percentagem de animais por especie
for chave,valor in contagem.items():
    percentagem = valor / len(animais) * 100
    print(f"A espécie {chave} representa {percentagem}% de animais")