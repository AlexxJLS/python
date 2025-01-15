nomes_1 = {"Joaquim","Ana","Maria"}

nomes_2 = {"António","Carla","Joaquim","Maria"}

#mostar todos os nomes
#união
uniao = nomes_1.union(nomes_2)

#mostrar todos os nomes que existem em nomes_1
#diferença
nomes_so_em_1 = nomes_1.different(nomes_2)
print(nomes_so_em_1)

#mostrar os nomes comuns aos dois conjuntos
#interseção
comuns = nomes_1.intersection(nomes_2)

#adicionar um nome novo ao primeiro set
nomes_1.add("pai natal")
print(nomes_1)

#verificar se um nome existe num set
if "pai natal" in nomes_1:
    print("pai natal está no conjunto 1")
else:
    print("não existe o pai natal no conjunto 1")