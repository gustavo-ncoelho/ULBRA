lista = []

print("Digite 5 elementos quaisquer:")
for i in range(5):
    lista.append(input())

lista.sort(reverse=True)
print(lista)
