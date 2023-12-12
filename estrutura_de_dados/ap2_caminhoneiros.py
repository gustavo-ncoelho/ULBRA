filaCaminhoneiros = []

def verificarFila(fila):
    if fila.size() == 0:
        return True
    else:
        return False

def desenfileirar(fila):
    filaVazia = verificarFila()
    if filaVazia == True:
        print('Fila está vazia')
    else:
        print(f'Caminhoreio {fila[0]} removido da fila')
        fila.pop(0)

def mostrarFila(fila):
    print(f'Os caminhoneiros que estão na fila são: {fila}')
        
