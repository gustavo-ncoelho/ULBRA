def obterNumeros():
    lista = []
    entrada = input("Digite números de uma lista separados por - : ").split("-")
    for i in entrada:
        try:
            numeros = float(i)
            lista.append(numeros)
        except ValueError:
            print(f"Valor {i} retirado da soma")
    return lista

def somarNumeros(lista):
    soma = 0
    for n in lista:
        soma += n
    return soma

lista = obterNumeros()
print(somarNumeros(lista))
