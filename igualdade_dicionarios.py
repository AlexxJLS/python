#Igualdade de dicionários
d1 = {'carro':'ford','preço':10000}
d2 = {'preço':10000,'carro':'ford'}
d3 = {'carro':'vw','preço':10000}
d4 = {'carro':'ford','preço':10000,'ano':2019}

print(d1==d2)   #iguais porque a ordem não interessa
print(d1==d3)
print(d1==d4)

d=d1
d['modelo'] = 'fiesta'
print(d==d1)