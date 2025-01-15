"""
Exercício com listas
-----------------------------------------------------------------------------------------------------------

1. Crie duas listas com nomes de sócios de dois clubes de futebol inseridos pelo utilizador.

2. Compare as duas listas e coloque numa terceira listas os nomes que são comuns aos dois clubes.

3. Para cada nome da terceira lista solicite ao utilizador em qual clube pretende permanecer e de acordo com a escolha deve remover o nome do outro clube.

4. No final deve listar ordenar as três listas e mostrar os nomes ao utilizador

-----------------------------------------------------------------------------------------------------------
"""

def AdicionarSocios(texto_clube):
    socios_clube = []
    while True:
        nome_socio = input(f"Insira o nome do sócio do {texto_clube}[prima Enter caso não haja mais]:")
        if nome_socio == "":
            print("\n")
            return socios_clube
        else:
            socios_clube.append(nome_socio)

def SociosComuns(clube1,clube2):
    set_clube1=set(clube1)
    set_clube2=set(clube2)
    set_clube1e2=set_clube1.intersection(set_clube2)
    clube1e2=list(set_clube1e2)
    return clube1e2

def RemoverDuplicados(repetidos,clube1,clube2):
    for i in range(len(repetidos)):
        op=input(f"Qual dos clubes pretende permanecer o/a sr. {repetidos[i]}?[1 ou 2]")
        socio_eliminar=repetidos[i]
        if op=="1":
            for i in range(len(clube2)):
                if clube2[i]==socio_eliminar:
                    print(f"O sócio {socio_eliminar} vai ser removido do Clube 2")
                    clube2.remove(socio_eliminar)
                    break
        elif op=="2":
            for i in range(len(clube1)):
                if clube1[i]==socio_eliminar:
                    print(f"O sócio {socio_eliminar} vai ser removido do Clube 2")
                    clube1.remove(socio_eliminar)
                    break
        else:
            print("Opção Inválida!")
            RemoverDuplicados(repetidos,clube1,clube2)

def Ordenar(clube):
    clube_ordenado=sorted(clube)
    return clube_ordenado

def Listar(clube,texto):
    print(f"Sócios {texto}:")
    for i in range(len(clube)):
        print(clube[i])
    print("\n")

def main():
    texto1="Clube 1"
    texto2="Clube 2"
    texto_repetidos="repetidos"
    clube1=AdicionarSocios(texto1)
    clube2=AdicionarSocios(texto2)
   
    repetidos=SociosComuns(clube1,clube2)
   
    RemoverDuplicados(repetidos,clube1,clube2)

    clube1_ordenado=Ordenar(clube1)
    clube2_ordenado=Ordenar(clube2)
    repetidos_ordenado=Ordenar(repetidos)

    Listar(clube1_ordenado,texto1)
    Listar(clube2_ordenado,texto2)
    Listar(repetidos_ordenado,texto_repetidos)

if __name__ == "__main__":
    main()