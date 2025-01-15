def AdicionarSocios(texto_clube):
    socios_clube = []
    while True:
        nome_socio = input(f"Insira o nome do sócio do {texto_clube}[prima Enter caso não haja mais]:")
        if nome_socio == "":
            return socios_clube
        else:
            socios_clube.append(nome_socio)
    
def RemoverSociosIguais(socios_sporting,socios_benfica):
    for i in range(len(socios_benfica) - 1,-1,-1):
        if socios_benfica[i] in socios_sporting:
            socios_sporting.remove(socios_benfica[i])
            nome =socios_benfica.pop(i)
            print(f"O nome {nome} foi removido por ser sócio de ambas as equipas")

def main():
    texto_sporting = "Sporting"
    texto_benfica = "Benfica"
    socios_sporting = AdicionarSocios(texto_sporting)
    socios_benfica = AdicionarSocios(texto_benfica)
    RemoverSociosIguais(socios_sporting,socios_benfica)
    print("Socios Sporting:",socios_sporting)
    print("Socios Benfica:",socios_benfica)
if __name__ == "__main__":
    main()