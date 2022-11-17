lista = []

for i in range(5):
    valor = int(input("Digite um número inteiro:\n"))
    lista.append(valor)

print(lista)

#soma dos valores da lista

total = 0

for i in range(5):
    total = total + lista[i]

print(total)

#com while fica:

lista2 = []
i = 0

while i<5:
    i += 1
    lista2.append(int(input("Digite um valor inteiro: \n")))

print(lista2)
    