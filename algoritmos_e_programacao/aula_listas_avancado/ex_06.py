lista = []
lista30 = []
soma30 = 0

print("Digite 8 valores inteiros:")
for i in range(8):
    lista.append(int(input()))

print(lista)

for x in lista:
    if x >= 30:
        lista30.append(x)
    else:
        continue

for z in lista30:
    soma30 = soma30 + z

print(f"Soma dos numeros maiores que 30 é {soma30}")

