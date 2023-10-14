username = "sadikturan"
password = "1234"

if (username == "sadikturan") and (password == "1234"):
    print("Hoş geldiniz")
else:
    print("kullanıcı isminiz ya da parolanız yanlış")


#girilen kullanıcı adından ya da paroladan hangisinin yanlış olduğunu belirtmek istiyorsak:
if(username == "sadikturan"):
    if (password == "1234"):
        print("Hoş geldiniz")
    else:
        print("parola yanlış")
else:
    print("username yanlış")