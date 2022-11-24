num = 0
soma = 0
quantImpares = 0
numLista = []

print("Digite quantos números inteiros quiser. Para parar a leitura dos dados, digite o número 0.")

while True:
    num = int(input())
    if num == 0:
        break
    elif num%2 == 0:
        print("Este número é par!!!")
    else:
        print("Esse número é ímpar!!!")
    numLista.append(num)

for n in numLista:
    soma = soma + n
    
print(f"\n A soma dos números digitados é: {soma}")

for i in numLista:
    if i%2 == 0:
        continue
    else:
        quantImpares += 1

print(f"\n São {quantImpares} números ímpares.")
