import random
import time

def menu():
    print('''
        ---- MENU: ----
        1 - Digitar número
        2 - Criar lista aleatório
        3 - Imprimir lista
        4 - Limpar lista
        5 - Ordenar por Selection Sort
        6 - Ordenar por Bubble Sort
        7 - Ordenar por Insertion Sort
        8 - Ordenar por Merge Sort
        9 - Ordenar por Quick Sort
        0 - SAIR''')

def opcao():
    while True:
        try:
            opcao = int(input('Digite uma opção: '))
        except ValueError:
            print('Opção inválida!!!')
            continue

        if opcao >= 0 and opcao <= 9:
            return opcao
        else:
            print('Opção inválida!!!')
            continue

def cronometro(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista)
    fim = time.time()
    tempo = fim - inicio
    print(f'Tempo de processamento: {tempo:.6f} segundos')

def enfileirar(lista):
    valor = int(input('Digite um número para enfileirar: '))
    lista.append(valor)

def enfileirarAleatorio(lista):
    qtd = int(input('Digite a quantidade de números desejada: '))
    for i in range(qtd):
        while True:
            aleatorio = random.randint(1, 1000)
            if aleatorio in lista:
                continue
            else:
                lista.append(aleatorio)
                break

def mostrarLista(lista):
    print(lista)

def selectionSort(lista):
    inicio = time.time()
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
    fim = time.time()
    tempo = fim - inicio
    print(f'O processo demorou {tempo:.8f} segundos')

def bubbleSort(lista):
    inicio = time.time()
    for i in range(len(lista)):
        for j in range(len(lista)-1, i, -1):
            if lista[j] < lista[j-1]:
                aux = lista[j]
                lista [j] = lista[j-1]
                lista[j-1] = aux
    fim = time.time()
    tempo = fim - inicio
    print(f'O processo demorou {tempo:.8f} segundos')

def insertionSort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        metadeEsquerda = lista[:meio]
        metadeDireita = lista[meio:]

        mergeSort(metadeEsquerda)
        mergeSort(metadeDireita)

        i = j = k = 0

        while i < len(metadeEsquerda) and j < len(metadeDireita):
            if metadeEsquerda[i] < metadeDireita[j]:
                lista[k] = metadeEsquerda[i]
                i += 1
            else:
                lista[k] = metadeDireita[j]
                j += 1
            k += 1

        while i < len(metadeEsquerda):
            lista[k] = metadeEsquerda[i]
            i += 1
            k += 1

        while j < len(metadeDireita):
            lista[k] = metadeDireita[j]
            j += 1
            k += 1

def quickSortResumido(lista):   #Aqui está sendo utilizado list comprehension
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores = [x for x in lista[1:] if x <= pivot]
        maiores = [x for x in lista[1:] if x > pivot]
        ordenados = quickSortResumido(menores) + [pivot] + quickSortResumido(maiores)
        return ordenados
    
def quickSort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores = []
        maiores = []

        for x in lista[1:]:
            if  x <= pivot:
                menores.append(x)
            else:
                maiores.append(x)
        
        menoresOrdenados = quickSort(menores)
        maioresOrdenados = quickSort(maiores)

        ordenados = menoresOrdenados + [pivot] + maioresOrdenados
        return ordenados



lista_original = []

while True:
    menu()
    opc = opcao()

    if opc == 0:
        break
    elif opc == 1:
        enfileirar(lista_original)
    elif opc == 2:
        enfileirarAleatorio(lista_original)
    elif opc == 3:
        mostrarLista(lista_original)
    elif opc == 4:
        lista_original = []
    elif opc == 5:
        cronometro(selectionSort, lista_original)
    elif opc == 6:
        cronometro(bubbleSort, lista_original)
    elif opc == 7:
        cronometro(insertionSort, lista_original)
    elif opc == 8:
        cronometro(mergeSort, lista_original)
    elif opc == 9:
        cronometro(quickSort, lista_original)

    
