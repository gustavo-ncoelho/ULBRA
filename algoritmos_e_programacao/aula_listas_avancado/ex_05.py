lista = []

print("Digite vários números inteiros, o programa irá encerrar quando 99 for digitado:")
while True:
    num = int(input())
    lista.append(num)
    if num == 99:
        break
    else:
        continue

soma = 0
lista_len = len(lista)
media = 0

for i in range(len(lista)):
    soma += lista[i]

print(f"soma: {soma}")

media = soma/lista_len
print(f"média: {media}")

print(f"Foram digitados {lista_len} valores")


