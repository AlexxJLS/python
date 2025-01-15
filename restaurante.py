lugares=100

        
while True:
    pessoas=int(input("Número de pessoas que entram:"))
    
    if pessoas==0:
        break
    
    if pessoas>lugares:
        print("Não é possivel entrar %d pessoas, porque só existem %d vagas"%(pessoas,lugares))
        continue
    
    lugares=lugares-pessoas
    print("Entraram %d pessoas, sobram %d lugares"%(pessoas,lugares))
