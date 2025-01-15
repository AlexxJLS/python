#Programa para sugerir a loja onde um cabaz de produtos é mais barato
#O utilizador insere um cabaz de produtos a comprar
#Se não existirem todos os produtos a comprar deve informar o utilizador
precos={
'Pingo Doce':{"Arroz": 1.18, "Maçã": 2.85, "Leite": 0.82, "Frango": 4.98, "Café": 22.9, "Água5l": 1.29, "Azeite": 9.90, "Sal grosso": 0.25, "Açucar": 7.30, "Salmão": 12.99},

'auchan':{"Frango":2.34,"Arroz":1.05,"Maçã":1.59,"Leite":0.80,"Azeite":12.68,"Água5l":1.05,"Água6l":0.84,"Sal grosso":2.29,"Salmão":24.93,"Açucar":1.79,"Café":6.59},

'continente':{"Arroz":1.83,"Maçã":1.99,"Leite":0.82,"Frango":1.25,"Café":6.59,"Água5l":1.05,"Água6l":0.84}}

def LerCompras():
    compras={}
    #ciclo infinito para parar apenas quando o utilizador inserir Enter
    while True:
        #input com a primeira letra maiuscula
        produto=input("Insira o produto").capitalize()
        #ver se o utilizador inseriu Enter
        if produto=="":
             break
        #se chamar a função e der False não existe o produto
        if not ProdutoExiste(produto):
             print("Produto não existente")
             continue
        quantidade=float(input("Quantidade a comprar:"))
        if quantidade<=0:
             print("Quantidade deve ser superior a 0")
             continue
        if produto in compras:
            compras[produto]+=quantidade
        else:
             compras[produto]=quantidade
    print(f"A sua lista de compras:{compras}")
    return compras

def QuantoCusta(loja,produto):
     produtos=precos[loja]
     if produto in produtos:
          return produtos[produto]
     return None

def ProdutoExiste(produto):
    #verificar se existe o produto
        for loja,produtos in precos.items():
            if produto in produtos:
                 return True
        return False

def LojaMaisBarata(compras):
    for loja in precos.keys():
         soma=0
         for produto,quantidade in compras.items():
            custo=QuantoCusta(loja,produto)
            if custo is None:
                print(f"A {loja} não tem {produto}")
                soma=-1
                break
            soma+=custo*quantidade
        #if soma<0:
         #   continue
        #if maisbarato is None or soma<maisbarato:
            maisbarato=soma
            LojaBarata=loja

         
              
def main():
     compras=LerCompras()
     loja,custo=LojaMaisBarata(compras)
     print(f"Loja mais barata {loja} e as suas compras vão custar {custo}")

if __name__=='__main__':
     main()