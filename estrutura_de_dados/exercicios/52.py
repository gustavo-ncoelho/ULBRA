lista = []
print("Digite os valores, e 0 para parar:")

while True:
    numero = float(input("Digite um valor: "))
    if numero == 0:
        break
    else:
        lista.append(numero)

numeroMenor = 9999999999999

for i in lista:
    if i < numeroMenor:
        numeroMenor = i
    else:
        continue

print(f'O número menor é {numeroMenor}')