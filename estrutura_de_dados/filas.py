def mostrarMenu():  
    print("""
        Esolha uma opção: 
        1 - ENFILEIRAR
        2 - DESENFILEIRAR
        3 - MOSTRAR PRIMEIRO DA FILA
        4 - MOSTRAR FILA
        5 - ENFILEIRAR PRIORITÁRIO
        6 - DESENFILEIRAR PRIORITÁRIO
        7 - MOSTRAR PRIMEIRO PRIORITÁRIO
        8 - MOSTRAR PRIORITÁRIOS
        9 - REALIZAR CHAMADA
        0 - SAIR
        """)

def enfileirar(lista, valor):
    print(f'Valor {valor} adicionado à fila')
    lista.append(valor)

def desenfileirar(lista, historico):
    if not lista:
        print('Fila vazia!')
    else:
        print(f'Valor {lista[0]} removido da fila')
        historico.append(lista[0])
        lista.pop(0)

def mostrarPrimeiro(lista):
    print(f'O primeiro valor da fila é {lista[0]}')

def mostrarTodos(lista):
    print(lista)

def chamada(lista, listaP,chamadaP, historico):
    if chamadaP == 0 or chamadaP == 1 or chamadaP == 2:
        if not listaP:
            print(f'Chamando fila normal: {lista[0]}')
            historico.append(lista[0])
            lista.pop(0)
        else:
            print(f'Chamando fila prioritária: {listaP[0]}')
            historico.append(listaP[0])
            listaP.pop(0)
            chamadaP += 1
    elif chamadaP == 3:
        print(f'Chamando fila normal: {lista[0]}')
        historico.append(lista[0])
        lista.pop(0)
        chamadaP = 0
    return chamadaP
    

fila = []
filaPrioritarios = []
historico = []
chamadaPrioritarios = 0

while True:
    # mostrarMenu()
    opcao = int(input('Digite a opcao desejada: '))
    
    if opcao == 1:
        valor = input('Enfileirar na fila normal: ')
        enfileirar(fila, valor)
    elif opcao == 2:
        desenfileirar(fila, historico)
    elif opcao == 3:
        mostrarPrimeiro(fila)
    elif opcao == 4:
        mostrarTodos(fila)
    elif opcao == 5:
        valorPrioritário = input('Enfileirar na fila prioritária: ')
        enfileirar(filaPrioritarios, valorPrioritário)
    elif opcao == 6:
        desenfileirar(filaPrioritarios)
    elif opcao == 7:
        mostrarPrimeiro(filaPrioritarios)
    elif opcao == 8:
        mostrarTodos(filaPrioritarios)
    elif opcao == 9:
        chamadaPrioritarios = chamada(fila, filaPrioritarios, chamadaPrioritarios, historico)
    elif opcao == 10:
        print(reversed(historico))
    elif opcao == 0:
        print('Programa encerrado, obrigado!!!')
        break
    else:
        print('Digite uma opcao válida!!!')
        continue
    

