#Igualdade em sets
conjunto_1 = {1,2,3,4,5}
conjunto_2 = {1,2,3,4,5}
conjunto_3 = {5,2,3,4,1}
conjunto_4 = {1,2,3,4,6}

print(conjunto_1 == conjunto_2)
print(conjunto_1 == conjunto_3)   #igual porque a ordem não interessa
print(conjunto_1 == conjunto_4)

novo = conjunto_1
novo.add(6)
print(novo == conjunto_1)
