
while True:
    dia=int(input("Insira o dia do ano:"))
    if dia>=1 and dia<=365:
        break

if dia>=356 or dia<=78:
    print("Inverno")

elif dia>=79 and dia<=171:
    print("Primavera")

elif dia>=172 and dia<=264:
    print("Verão")

else:
    print("Outono")