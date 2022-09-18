num = int(input("Digite o seu número: "))
num_hras = int(input("Digite o número de horas de trabalho por semana: "))
valor_hra = float(input("Digite o valor recebido por hora de trabalho: "))
num_filhos = int(input("Informe a quantidade de dependentes inferiores a 14 anos: "))
idade = int(input("Digite sua idade: "))
sal_familia = float(input("Digite o valor recebido de salário família por filho: "))

sal_familia_total = sal_familia*num_filhos
sal_bruto = (num_hras*4*valor_hra)+sal_familia_total
desc_inss = sal_bruto*0.085

if sal_bruto > 1500:
    desc_ir = sal_bruto*0.15
    sal_liquido = sal_bruto-desc_inss-desc_ir
elif sal_bruto > 500 and sal_bruto <= 1500:
    desc_ir = sal_bruto*0.08
    sal_liquido = sal_bruto-desc_inss-desc_ir
elif sal_bruto <= 500:
    desc_ir = 0
    sal_liquido = sal_bruto-desc_inss-desc_ir

print("Funcionário número " + str(num) + ":")
print("Seu salário bruto é de " + str(sal_bruto) + "R$")
print("O total a ser descontado do seu salário é de " + str(desc_inss+desc_ir) + "R$")
print("O seu salário líquido total é de " + str(sal_liquido) + "R$")


