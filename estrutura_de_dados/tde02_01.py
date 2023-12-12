def somaPares(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    return soma

entrada = input("Digite valores separados por vírgula: ")

numeros = []
entradaTratada = entrada.split(",")
for num in entradaTratada:
    try:
        numeros.append(int(num))
    except ValueError:
        print(f'Ignorado o valor {num}')

resultado = somaPares(numeros)
print(f'A soma dos números pares é: {resultado}')

