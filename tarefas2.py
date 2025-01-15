'''
PSI - Módulo 5
Estruturas de Dados Compostas
Coleções
'''

# Estrutura de dados
Disciplina_PSI={
                  'Modulos': ('Algoritmia','Estruturas de Controlo','Funções','Estruturas de Dados Estáticas'),
                  'WebGrafia':{'3wschool.com','github.com/alunosnet','udacity.com'} ,
                  'Aulas':['M1','M1','M1','M2','M2','M3','M3','M4','M4','M4','M4'],
                  'Avaliação':['Teste Escrito','Teste prático','Teste prático','Teste prático']
               }

# Mostrar os sites recomendados para a disciplina (webgrafia)
print(Disciplina_PSI['WebGrafia'])

# Mostrar o nome de um módulo pela posição (pedir ao utilizador)
pos=int(input("Insira a posição do modulo [1-4]"))
pos-=1
print(Disciplina_PSI['Modulos'][pos])

# Mostrar as aulas que são dadas num módulo (pedir ao utilizador o nº do módulo)
modulo=int(input("Insira o número do modulo [1-4]:"))
modulostr = f"{modulo}"

for i in range(len(Disciplina_PSI['Aulas'])):
    if modulostr in Disciplina_PSI['Aulas'][i]:
        print(Disciplina_PSI['Aulas'][i])

# Mostrar os módulos que tenham determinado conteudo (pedir ao utilizador)
conteudo = input("Insira o conteudo:")

for i in range(len(Disciplina_PSI['Modulos'])):
    if conteudo in Disciplina_PSI['Modulos'][i]:
        print(Disciplina_PSI['Modulos'][i])

# Mostrar os módulo cuja avaliação não é 'Teste Escrito'
print("Não é avaliação em teste escrito:")
for i in range(len(Disciplina_PSI['Avaliação'])):
    if 'Escrito' not in Disciplina_PSI['Avaliação'][i]:
        print(f"Modulo{i+1}")

# Mostrar o nº de módulos da disciplina
soma = 0
for i in range(len(Disciplina_PSI['Modulos'])):
    soma += 1
print(f"Existem {soma} modulos")

# Adicionar mais 5 aulas do módulo M2
for i in range(5):
    Disciplina_PSI['Aulas'].append("M2")
