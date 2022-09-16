ndias = int(input("Digite a quantidade de dias que deseja ficar hospedado: "))

valor_total = ndias * 50

if ndias < 15:
    valor_total = valor_total + (ndias*1.5)
elif ndias == 15:
    valor_total = valor_total + (ndias*1)
elif ndias > 15:
    valor_total = valor_total + (ndias*0.5)

print("O valor total a ser pago será de " + str(valor_total) + "R$")