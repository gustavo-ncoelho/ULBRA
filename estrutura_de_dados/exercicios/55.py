lista = []
print("Digite os valores, e 0 para parar:")

while True:
    numero = int(input("Digite um valor: "))
    if numero == 0:
        break
    else:
        lista.append(numero)

multiplos = []

for i in lista:
    if i % 3 == 0 and i % 5 == 0:
        multiplos.append(i)
    else:
        continue

print(f'Os múltiplos de 3 e 5 são: {multiplos}')