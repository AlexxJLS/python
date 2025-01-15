lugares=100
mesas=20
        
while True:
    pessoas=int(input("Número de pessoas que entram:"))
    
    if pessoas==0:
        break
    
    if pessoas>lugares:
        print("Não é possivel entrar %d pessoas, porque só existem %d vagas"%(pessoas,lugares))
        continue
    
    if mesas<=0:
        print("Não há mais mesas")
        continue
    
    lugares=lugares-pessoas
    mesas=mesas-1
    print("Entraram %d pessoas, sobram %d lugares"%(pessoas,lugares))
    print("Sobram %d mesas"%mesas)

