print("Digite 1 para plano de 300MB por R$99,90")
print("Digite 2 para plano de 400MB por R$109,90")

plano = int(input())

if plano == 1:
    valor_plano = 99.90
    print("Você escolheu o plano de 300Mb")
elif plano == 2:
    valor_plano = 109.90
    print("Você escolheu o plano de 400Mb")
elif plano < 1 or plano > 2:
    print("Erro, escolha um plano válido")
    print(valor_plano)

metros = int(input("Digite a quantidade de metros de cabo necessário para a sua instalação: "))

valor_metros = metros * 3

sub_total = valor_plano + valor_metros

if sub_total <= 500:
    valor_total = sub_total + (metros*15)
    print("Obrigatório compra do cabo blindado. O valor total será de " + str(valor_total) + "R$")
elif sub_total > 500:
    valor_total = sub_total
    print("Não obrigatório a compra do cabo blindado. O valor total será de " + str(valor_total) + "R$")

