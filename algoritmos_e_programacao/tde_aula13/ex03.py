idades = []
alturas = []
pesos = []
n = 1

for z in range(3):
    print(f"\nPessoa número {n}")
    idades.append(int(input("Digite a idade: ")))
    alturas.append(float(input("Digite a altura: ")))
    pesos.append(float(input("Digite o peso: ")))
    n += 1

# num_idade = 0

# for idade in idades:
#     if idade >= 50:
#         num_idade += 1
#     else:
#         continue

index = []

for idade in idades:
    if idade >= 10 and idade <= 20:
        index.append(idades.index(idade))
    else:
        continue



