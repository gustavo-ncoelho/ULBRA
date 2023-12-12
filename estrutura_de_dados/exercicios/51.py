lista = []
print("Digite os valores, e 0 para parar:")

while True:
    numero = int(input("Digite um valor: "))
    if numero == 0:
        break
    else:
        lista.append(numero)

numeroMaior = 0

for i in lista:
    if i > numeroMaior:
        numeroMaior = i
    else:
        continue

print(f'O número maior é {numeroMaior}')