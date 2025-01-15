#calcular a quantia total a receber
#ler os dias e os km
d=float(input("Nº de dias:"))
km=float(input("Nº de km:"))


if d<1:
    d=1

#calcular o total sem IVA
s_iva=10*d+km*0.60

#calcular o total com IVA
c_iva=s_iva+s_iva*0.23
print("A quantia total é",c_iva)

