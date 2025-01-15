F1=float(input("Número de fatias da primeira pessoa:"))
F2=float(input("Número de fatias da segunda pessoa:"))
F3=float(input("Número de fatias da terceira pessoa:"))
preço=float(input("Preço da pizza:"))

TF=F1+F2+F3
PF1=F1/TF
PF2=F2/TF
PF3=F3/TF

print("Primera pessoa paga",PF1*preço)
print("Segunda pessoa paga",PF2*preço)
print("Terceira pessoa paga",PF3*preço)