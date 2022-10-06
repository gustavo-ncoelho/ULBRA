while True:
    print("Digite sua senha: ")
    senha = input()
    if senha == "123456789":
        print("Acesso liberado!!!")
        break
    else:
        print("Acesso negado, tente novamente!!!")

print("Bem vindo!!!")