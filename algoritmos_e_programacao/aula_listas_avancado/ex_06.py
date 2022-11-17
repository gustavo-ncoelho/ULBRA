lista = []
lista30 = []
soma30 = 0

print("Digite 8 valores inteiros:")
for i in range(8):
    lista.append(input())

print(lista)

for x in lista:
    if x >= 30:
        lista30.append(x)
    else:
        continue

for z in lista30:
    soma = soma + z

print(f"Soma dos numeros")

