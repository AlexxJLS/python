base=int(input("Insira a base:"))
expoente=int(input("Insira o expoente:"))

total=1
for i in range(expoente):
    total=total*base
print(total)