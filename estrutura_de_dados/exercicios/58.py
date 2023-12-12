lista = []
print("Digite os valores, e 0 para parar:")

while True:
    numero = int(input("Digite um valor: "))
    if numero == 0:
        break
    else:
        lista.append(numero)

print(lista)

def procurarNumero(num):
    encontrado = None

    for i in lista:
        if i == num:
            encontrado = True
            break
        elif i != num:
            encontrado = False
            continue

    if encontrado == True:
        print(f"O número {num} foi encontrado!!!")
    else:
        print('O número NÃO foi encontrado!!!')

procurarNumero(int(input("Digite o número que deseja procurar: ")))