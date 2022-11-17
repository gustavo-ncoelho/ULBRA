lista = []

print("Digite cinco números inteiros: ")
for i in range(5):
    lista.append(int(input()))


print(lista)
soma = 0

for i in range(5):
    soma += lista[i]

print(soma)