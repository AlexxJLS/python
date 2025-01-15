turma = {
    123:{'M01':10,'M02':15,'M03':8},
    124:{'M01':10,'M02':15,'M03':18},
    125:{'M01':12,'M02':11,'M03':10}
}

#Mostrar as notas dos alunos, primeiro deve mostrar o nrprocesso e depois a nota de cada módulo
for nprocesso,notas in turma.items():
    print(f"{nprocesso=}")
    for modulo,nota in notas.items():
        print(f"{modulo=} - {nota=}")
print("-*20")  

#Calcular e mostrar a média das notas por aluno
for nprocesso,notas in turma.items():
    print(f"{nprocesso=}")
    notas_aluno = notas.values()
    media = sum(notas_aluno) / len(notas_aluno)
    print(f"{nprocesso=} - média = {media:.2f}")

#Calcular e mostrar o nº de postivas e negativas por aluno
for nprocesso,notas in turma.items():
    notas_aluno = notas.values()
    positivas = 0
    for nota in notas_aluno:
        if nota >= 10:
            positivas += 1
        else:
            print(f"{nprocesso=} - positivas = {positivas} - negativas = {len(notas_aluno) - positivas}")

#Calcular e mostrar qual o aluno com melhor média
melhor = 0
for nprocesso,notas in turma.items():
    print(f"{nprocesso=}")
    notas_aluno = notas.values()
    media = sum(notas_aluno) / len(notas_aluno)
    if media  > melhor:
        melhor = media
        melhor_nprocesso = nprocesso
print(f"{melhor_nprocesso=} - melhor média = {melhor:.2f}")