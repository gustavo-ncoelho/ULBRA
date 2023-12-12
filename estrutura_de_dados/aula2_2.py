numeros_validos = []
soma = 0
entrada = input("Digite uma lista de números separados por espaços: ").split() #split() transforma uma sequencia de dados em uma lista

for item in entrada:
    try:
        numero = float(item)
        numeros_validos.append(numero)
    except ValueError:
        print(f"Valoor invalido: {item} (IGNORADO)")

for n in numeros_validos:
    soma += n

print(soma)