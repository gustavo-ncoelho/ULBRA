faturamento = float(input("Digite o  valor do faturamento total da sua empresa: "))
custos = float(input("Digite o valor dos custos de produção: "))

pis = faturamento*0.0065
cofins = faturamento*0.03
lucro = faturamento-(pis+cofins+custos)

print("O seu faturamento é de " + str(faturamento) + "R$")
print("O valor pago de PIS é de " + str(pis) + "R$")
print("O valor pago do COFINS " + str(cofins) + "R$")
print("O lucro total da sua empresa é de " + str(lucro) + "R$")