# Desafio:
# Criar um algoritmo que recebe um número ou sequência de números, separados por virgula.
# Os números devem ser inteiros, e armazenados em uma lista.
# O algoritmo deve ter um menu:
# 1- Adicionar números
# 0 - Sair
lista = []

while True:

    print("MENU: \n (1) Adicionar valor \n (2) Remover último \n (3) Limpar lista \n (4) Impirmir lista \n (5) Imprimir ultimo valor \n (0) Sair")

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        entrada = input("Digite valores separados por vírgula: ").split(',')
        for i in entrada:
            try:
                num = int(i)
                lista.append(num)
            except ValueError:
                print(f'Valor {i} inválido')
                continue
    elif opcao == 2:
        lista.pop()
    elif opcao == 3:
        lista.clear()
    elif opcao == 4:
        print(lista)
    elif opcao == 5:
        print(lista[-1])
    elif opcao == 0:
        break
    else:
        print("Digite uma opção válida!!!")
        continue
    
    
