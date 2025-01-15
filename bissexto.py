a=int(input("Ano que pretende introduzir:"))

if (a%4==0 and a%100!=0) or a%400==0:
    print("É um ano bissexto")
else:
    print("Não é ano bissexto")
    