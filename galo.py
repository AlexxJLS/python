def DesenharTabuleiro(tabuleiro):
    for letra in tabuleiro:
        if letra == "|":
            print("")
        else:
            print(letra,end = "")
    print(" ")

def LerJogada(jogador,tabuleiro):
    linha = int(input("Linha:"))
    coluna = int(input("Coluna:"))
    posicao = int(input("Posição:"))
    return tabuleiro

def Vitoria():
    pass


def main():
    jogador = "X"
    tabuleiro = "---|---|---"
    DesenharTabuleiro(tabuleiro)
    while True:
        tabuleiro = LerJogada(jogador,tabuleiro)
        DesenharTabuleiro(tabuleiro)
        if Vitoria(tabuleiro):
            break
        if jogador == "X":
            jogador == "O"
        else:
            jogador == "X"

if __name__ == "__main__":
    main()
