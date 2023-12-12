class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def chamar(self):
        if len(self.itens) != 0:
            print(f'Chamando {self.itens[0]}')
            self.itens.pop(0)
        else:
            return print('Lista vazia')

    def topo(self):
        if len(self.itens) != 0:
            return self.itens[0]
        else:
            return print('Lista vazia')

fila = Fila()

while True:

    print('''
    1 - Enfileirar
    2 - Desenfileirar
    3 - Mostrar primeiro
    0 - Sair 
        ''')
    
    opcao = int(input('Escolha a opção: '))
    
    if opcao == 1:
        valor = input('Enfileirar: ')
        fila.enfileirar(valor)
    elif opcao == 2:
        fila.chamar()
    elif opcao == 3:
        print(fila.topo())
    elif opcao == 0:
        print('Programa encerrado, obrigado!!!')
        break
    else:
        print('Digite uma opcao válida!!!')
        continue