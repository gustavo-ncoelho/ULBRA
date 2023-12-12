pilha = []
deletados = []

def iniciarSistema():
    print("""
          PILHAS
          """)   
    print("""
          1 - EMPILHAR
          2 - DESEMPILHAR
          3 - LIMPAR
          4 - EXIBIR TOPO
          5 - EXIBIR PILHA
          6 - EXIBIR ÚLTIMO DELETADO
          7 - EXIBIR DELETADOS
          8 - REEMPILHAR DELETADO
          9 - DESEMPILHAR VÁRIOS
          0 - SAIR
          """)

def push(pilha):
    numeros = input('Digite valores que deseja empilhar, separados por vírgula (","): ')
    numeros = numeros.split(",")
    for i in numeros:
        pilha.append(i)

def pop(pilha,pilhaDel):
    if not pilha:
        print("Esta pilha está vazia!")
    else:
        print(f'Valor {pilha[-1]} removido da pilha!')
        pilhaDel.append(pilha[-1])
        pilha.pop()

def clear(pilha):
    pilha = []
    print(f'{pilha} agora está vazia!')

def peek(pilha):
    print(f'{pilha[-1]} está no topo da pilha!')

def show(pilha):
    if not pilha:
        print('Pilha está vazia!')
    else:
        for i in reversed(pilha):
            print(i)

def showLastDeleted(pilhaDel):
    if not pilhaDel:
        print('Pilha está vazia!')
    else:
        print(f'O último valor deletado foi {pilhaDel[-1]}')

def showDeleted(pilhaDel):
    if not pilhaDel:
        print('Pilha está vazia!')
    else:
        for i in reversed(pilhaDel):
            print(i)

def reempilharDeletado(pilha,pilhaDel):
    print(f'{pilhaDel[-1]} foi reempilhado')
    pilha.append(pilhaDel[-1])
    pilhaDel.pop()

def popMany(pilha,pilhaDel,valor):
    for i in range(valor):
        print(f'{pilha[-1]} foi removido da pilha!')
        pilhaDel.append(pilha[-1])
        pilha.pop()

while True:

    iniciarSistema()
    try:
        condition = int(input('Digite a opção desejada: '))
    except ValueError:
        print('Digite um valor válido')
        continue
    
    if condition == 1:
        push(pilha)
    elif condition == 2:
        pop(pilha,deletados)
    elif condition == 3:
        clear(pilha)
    elif condition == 4:
        peek(pilha)
    elif condition == 5:
        show(pilha)
    elif condition == 6:
        showLastDeleted(deletados)
    elif condition == 7:
        showDeleted(deletados)
    elif condition == 8:
        reempilharDeletado(pilha,deletados)
    elif condition == 9:
        valor = int(input('Quantos valores deseja desempilhar ?'))
        popMany(pilha,deletados,valor)
    elif condition == 0:
        print('Código encerrado!!!')
        break
    else:
        print('Digite um valor válido!')
        continue
