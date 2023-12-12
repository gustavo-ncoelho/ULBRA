def menu():
    print('''
        1 - Adicionar ao início
        2 - Adicionar ao final
        3 - Exibir primeiro
        4 - Exibir último
        5 - Remover primeiro
        6 - Remover último
        0 - Sair
        ''')

def addInicio(lista, valor):
    lista.insert(0, valor)
    print(f'{valor} foi inserido ao início do deck')
def addFinal(lista, valor):
    lista.append(valor)
    print(f'{valor} foi inserido ao final do deck')
def exibirPrimeiro(lista):
    print(f'O primeiro valor é {lista[0]}')
def exibirUltimo(lista):
    print(f'O último valor é {lista[-1]}')
def removerPrimeiro(lista):
    print(f'{lista[0]} foi removido do deck')
    lista.pop(0)
def removerUltimo(lista):
    print(f'{lista[-1]} foi removido do deck')
    lista.pop()

deck = []

while True:
    menu()
    try:
        opc = int(input('Digite a opção desejada: '))
    except ValueError:
        print('Digite um número inteiro entre 1 e 6 ou 0!!!')
        continue
    if opc == 1:
        valor = input('Digite o valor que deseja adicionar: ')
        addInicio(deck, valor)
    elif opc == 2:
        valor = input('Digite o valor que deseja adicionar: ')
        addFinal(deck, valor)
    elif opc == 3:
        exibirPrimeiro(deck)
    elif opc == 4:
        exibirUltimo(deck)
    elif opc == 5:
        removerPrimeiro(deck)
    elif opc == 6:
        removerUltimo(deck)
    elif opc == 0:
        print('Programa encerrado!!!')
        break
    else:
        print('Digite uma opção válida!!!')
        continue