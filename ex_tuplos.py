#Alexandre José Leandro Santos

#1. Crie um tuplo com os nome dos meses do ano.

meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')

#2. Imprima o terceiro mês do ano.

print(meses[2])

#3. Obtenha o tuplo dos meses do Verão

verao = meses[5:8]

#4. Verifique se "Junho" está presente no tuplo de meses

if "junho" in verao:
    print("Junho é no Verão")
else:
    print("Junho não é no Verão")

#5. Concatene 2 tuplos de cores.

cores_primarias = ('Vermelhos','Verde','Azul')
cores_secundarias = ('Laranja','Violeta','Amarelo')
cores = cores_primarias + cores_secundarias

#6. Repita o tuplo de cores 3 vezes

cores_3x = cores * 3

#7. Crie um tuplo com 5 elementos, onde o primeiro e o ultimo são iguais

tuplo = (5,2,1,3,5)

#8. Encontre o índice da primeira ocorrência de "Verde na tupla de cores."

pos = cores.index("Verde")

#9. Conte quantas vezes a letra "a" aparece na tupla de palavras

palavras = ('bla','maria','adeus')

soma = 0
for elemento in palavras:
    n = elemento.count('a')
    soma += n
print(soma)

#10. Ordene um tuplo de números em ordem crescente

numeros = (4,3,2,5,7,8)

numeros_ordenados = sorted(numeros)