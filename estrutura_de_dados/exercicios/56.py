lista = []
print("Digite os valores, e 0 para parar:")

while True:
    numero = int(input("Digite um valor: "))
    if numero == 0:
        break
    else:
        lista.append(numero)

lista.sort()
print(lista)