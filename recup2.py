email=input("Email:")
password=input("Password:")

temNumeros=False
temMinusculas=False
temMaiusculas=False

for c in password:
    if c>="0" and c<="9":
        temNumeros=True
    if c>="a" and c<="z":
        temMinusculas=True
    if c>="A" and c<="Z":
        temMaiusculas=True

if temNumeros==False or temMinusculas==False or temMaiusculas==False:
    print("Password não é segura poruqe deve ter letra minusculas, maiusculas e números")

if len(password)<8:
    print("Passwrod não é segura poriqe não tem 8 letras")

if password in email:
    print("Password não é segura porque faz parte do email")