# Elabore um algoritmo para calcular a média de idade de um número indeterminado de pessoas. 
# O programa deve encerrar quando a idade digitada for 0. Ao encerrar o programa deve mostrar 
# quantas leituras foram realizadas.

soma = 0
media = 0
qtdLeituras = 0
idade = 0
condicao = True

print("Digite quantas idades desejar para saber a média, para encerrar digite 0!!!")
while condicao == True:
    idade = (int(input()))
    if idade == 0:
        condicao = False
    else:
        qtdLeituras += 1
        soma += idade

media = soma / qtdLeituras

print(f"A média das idades é {int(media)} \n")
print(f"Foram realizadas {qtdLeituras} leituras")
