def notas(lista_nota,nr_notas):
    #melhor e pior nota
    melhor_nota = lista_nota[0]
    pior_nota = 200
    for i in range(nr_notas):
        if lista_nota[i] > melhor_nota:
            melhor_nota = lista_nota[i]
        if lista_nota[i] < pior_nota:
            pior_nota = lista_nota[i]

    #media
    soma = 0
    for i in range(nr_notas):
        soma += lista_nota[i]
    media = soma / nr_notas
    
    #Aprovado ou Reprovado
    if media >= 10:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    notas_aluno = {'nr_notas':nr_notas,'melhor_nota':melhor_nota,'pior_nota':pior_nota,'media':media,'situacao':situacao}
    return notas_aluno

def main():
    nr_notas = int(input("Quantas notas vai inserir?:"))
    lista_notas = []
    for i in range(nr_notas):
        nota = int(input(f"Insira a {i+1}ª nota:"))
        lista_notas.append(nota)

    print(notas(lista_notas,nr_notas))


if __name__ == "__main__":
    main()