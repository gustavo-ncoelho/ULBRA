soma = 0

for x in range(10):
    valor = float(input("Digite um valor:\n"))
    soma =  valor + soma

print(f"A soma dos números digitados é {soma}")

print("----------------------------")

soma_total = 0
numeros = []

while len(numeros) != 10:
    numeros.append(float(input("Digite um número:\n")))

for x in numeros:
    soma_total += x

print(f"\nA soma total dos números é: {soma_total}")