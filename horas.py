classe=int(input("Indique a sua classe com o número 1 ou 2:"))
horas=int(input("Indique quantas horas trabalhou:"))

if classe>=1 and classe<=2:
    p_horas=100
    p_horas_ext=120
    if classe==2:
        p_horas=200
        p_hora_ext=240
    horas_ext=horas-40
    if horas_ext<0:
        horas_ext==0
    salario=p_horas*(horas-horas_ext)+p_horas_ext*horas_ext
    print(salario)
else:
    print("A classe indicada não é valida!")


