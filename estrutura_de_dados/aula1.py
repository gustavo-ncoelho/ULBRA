lista = []

print("""MENU DE OPÇÕES \n 1 - PARA INSERIR \n 2 - REMOVER O ÚLTIMO \n 3 - REMOVER O PRIMEIRO\n 
4 - INSERIR NO INICIO \n 5 - IMPRIMIR A LISTA \n 6 - IMPRIMIR ÚLTIMO \n 7 - REMOVER ÍMPARES \n 
8 - REMOVER PARES \n 0 - SAIR""")

while True:
    opc = int(input("Digite a opção: "))

    if opc == 0:
        break
    elif opc == 1:
        num = int(input("Digite o valor: "))
        lista.append(num)
    elif opc == 2:
        lista.pop()
    elif opc == 3:
        lista.pop(0)
    elif opc == 4:
        num = int(input("Digite o valor: "))
        lista.insert(0, num)
    elif opc == 5:
        print(lista)
    elif opc == 6:
        print(lista[-1])
    elif opc == 7:
        for x in lista:
            if x % 2 == 1:
                lista.remove(x)
    elif opc == 8:
        for x in lista:
            if x % 2 == 0:
                lista.remove(x)
    else:
        print("Digite uma opção válida")
