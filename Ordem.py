#Um programa que lê 3 números e mostra-os por ordem crescente

n1=int(input("Introduza o primeiro número:"))
n2=int(input("Introduza o segundo número:"))
n3=int(input("Introduza o terceiro número:"))

#n1 é o maior?
if n1>n2 and n1>n3:
    maior=n1
    if n2>n3:
        menor=n3
        outro=n2
    else:
        menor=n2
        outro=n3
else:   #n2 é o maior?
    if n2>n1 and n2>n3:
        maior=n2
        if n1>n3:
            menor=n3
            outro=n1
        else:
            menor=n1
            outro=n3
    else:   #n3 é o maior?
        maior=n3
        if n1>n2:
            menor=n2
            outro=n1
        else:
            menor=n1
            outro=n2

print(menor,outro,maior)
