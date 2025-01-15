"""Codificar e Descodificar códigos"""
#variavel global
alfabeto = "abcdefghijklmnopqrstuvwxyz"
codigo = "bcdefghijklmnopqrstuvwxyza"

def Codificar(texto):
    texto = texto.lower()
    global alfabeto, codigo
    codificado = ""
    for letra in texto:
        if letra in alfabeto:
            posicao = alfabeto.index(letra)
            codificado = codificado + codigo[posicao]
        else:
            codificado = codificado + letra
    return codificado
    

def Descodificar(texto):
    texto = texto.lower()
    global alfabeto, codigo
    descodificado = ""
    for letra in texto:
        if letra in codigo:
            posicao = codigo.index(letra)
            descodificado = descodificado + alfabeto[posicao]
        else:
            descodificado = descodificado + letra
    return descodificado
    

def main():
    print(Codificar("xupa-me o rabo"))
    print(Descodificar("yvqb-nf p sbcp"))    
    
if __name__ == "__main__":
    main()