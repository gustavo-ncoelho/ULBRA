import sys

print("Para avaliação do seu Risco Coronário, digite os seguintes dados: ")

# GÊNERO:

print("Digite 1 se você for nascido HOMEM")
print("Digite 2 se você for nascido MULHER")
genero = int(input())

if genero != 1 and genero != 2:
    print("Valor inválido, por favor reinicie o programa!!!")
    sys.exit()
else:
    print()

#### ENTRADA DE VARIÁVEIS: ####

idade = int(input("Digite sua idade: "))
heranca_fam = int(input("Digite a quantidade de parentes com cardiopatia: "))
percent_gord = float(input("Digite o seu percentual de gordura: "))
tabagismo = int(input("Digite a quantidade de cigarros que você fuma por dia: "))
ex_hora_semana = int(input("Digite quantas horas você pratica exercícios físicos por semana: "))
ex_min_semana = ex_hora_semana*60
colesterol = int(input("Digite o seu colesterol: "))
pressao_sist = float(input("Digite sua pressão arterial sistólica: "))
pressao_diast = float(input("Digite a sua pressão arterial diastólica: "))

#### CONTAGEM DOS PONTOS: ####

pontos_idade = 0
pontos_heranca = 0
pontos_perc_gord = 0
pontos_tabagismo = 0
pontos_ex_min_semana = 0
pontos_colesterol = 0
pontos_pressao_sist = 0
pontos_pressao_diast = 0

# Idade:
if idade >= 10 and idade <= 20:
    pontos_idade = 1
elif idade >= 21 and idade <= 30:
    pontos_idade = 2
elif idade >= 31 and idade <= 40:
    pontos_idade = 3
elif idade >= 41 and idade <= 50:
    pontos_idade = 4
elif idade >=51 and idade <= 60:
    pontos_idade = 6
elif idade > 60:
    pontos_idade = 8

# Herança Familiar:
if heranca_fam == 0:
    pontos_heranca = 1
elif heranca_fam == 1:
    pontos_heranca = 2
elif heranca_fam == 2:
    pontos_heranca = 3
elif heranca_fam == 3:
    pontos_heranca = 7
elif heranca_fam == 4:
    pontos_heranca = 7
elif heranca_fam >= 5:
    pontos_heranca = 7

# Percentual de Gordura:
if genero == 1:
    if percent_gord <= 12:
        pontos_perc_gord = 0
    elif percent_gord > 12 and percent_gord <= 15.99:
        pontos_perc_gord = 1
    elif percent_gord > 16 and percent_gord <= 19.99:
        pontos_perc_gord = 2
    elif percent_gord > 20 and percent_gord <= 21.99:
        pontos_perc_gord = 3
    elif percent_gord > 22 and percent_gord <= 29.99:
        pontos_perc_gord = 5
    elif percent_gord > 30:
        pontos_perc_gord = 7
elif genero == 2:
    if percent_gord <= 16:
        pontos_perc_gord = 0
    elif percent_gord > 16 and percent_gord <= 19.99:
        pontos_perc_gord = 1
    elif percent_gord > 20 and percent_gord <= 24.99:
        pontos_perc_gord = 2
    elif percent_gord > 25 and percent_gord <= 32.99:
        pontos_perc_gord = 3
    elif percent_gord > 33 and percent_gord <= 39.99:
        pontos_perc_gord = 5
    elif percent_gord > 40:
        pontos_perc_gord = 7

# Tabagismo:
if tabagismo == 0:
    pontos_tabagismo = 0
elif tabagismo >= 0 and tabagismo <= 10:
    pontos_tabagismo = 1
elif tabagismo >= 11 and tabagismo <= 20:
    pontos_tabagismo = 2
elif tabagismo >= 21 and tabagismo <= 30:
    pontos_tabagismo = 3
elif tabagismo >= 31 and tabagismo <= 40:
    pontos_tabagismo = 6
elif tabagismo > 40:
    pontos_tabagismo = 8

# Minutos de Exercício por Semana:
if ex_min_semana > 240:
    pontos_ex_min_semana = 0
elif ex_min_semana >= 120  and ex_min_semana <= 240 :
    pontos_ex_min_semana = 1
elif tabagismo >= 80 and ex_min_semana <= 119:
    pontos_ex_min_semana = 2
elif ex_min_semana >= 60 and ex_min_semana <= 79:
    pontos_ex_min_semana = 3
elif ex_min_semana >= 31 and ex_min_semana <= 59:
    pontos_ex_min_semana = 6
elif ex_min_semana < 30:
    pontos_ex_min_semana = 8

# Colesterol:
if colesterol <= 180:
    pontos_colesterol = 1
elif colesterol >= 181 and colesterol <= 205:
    pontos_colesterol = 2
elif colesterol >= 206 and colesterol <= 230:
    pontos_colesterol = 3
elif colesterol >= 231 and colesterol <= 255:
    pontos_colesterol = 4
elif colesterol >= 256 and colesterol <= 280:
    pontos_colesterol = 5
elif colesterol > 280:
    pontos_colesterol = 7

# Pressão Arterial Sistólica:
if pressao_sist < 120:
    pontos_pressao_sist = 1
elif pressao_sist >= 120 and pressao_sist <= 139:
    pontos_pressao_sist = 2
elif pressao_sist >= 140 and pressao_sist <= 159:
    pontos_pressao_sist = 3
elif pressao_sist >= 160 and pressao_sist <= 179:
    pontos_pressao_sist = 4
elif pressao_sist >= 180 and pressao_sist <= 199:
    pontos_pressao_sist = 6
elif pressao_sist >= 200:
    pontos_pressao_sist = 8

# Pressão Arterial Diastólica:
if pressao_diast <= 70:
    pontos_pressao_diast = 1
elif pressao_diast >= 71 and pressao_diast <= 76:
    pontos_pressao_diast = 2
elif pressao_diast >= 77 and pressao_diast <= 82:
    pontos_pressao_diast = 3
elif pressao_diast >= 83 and pressao_diast <= 93:
    pontos_pressao_diast = 4
elif pressao_diast >= 94 and pressao_diast <= 105:
    pontos_pressao_diast = 6
elif pressao_diast >= 106:
    pontos_pressao_diast = 8

#### PONTUAÇÃO ####

pontuacao = (pontos_idade + 
             pontos_heranca + 
             pontos_perc_gord + 
             pontos_tabagismo + 
             pontos_ex_min_semana + 
             pontos_colesterol + 
             pontos_pressao_sist + 
             pontos_pressao_diast)

#### RESULTADO FINAL ####

if pontuacao >= 5 and pontuacao <= 11:
    print("Você somou " + str(pontuacao) + " pontos e")
    print("seu risco cardiovascular é bem abaixo da média.")
    print("Parabéns!!!")
elif pontuacao >= 12 and pontuacao <= 17:
    print("Você somou " + str(pontuacao) + " pontos e")
    print("seu risco cardiovascular é abaixo da média.")
elif pontuacao >= 18 and pontuacao <= 24:
    print("Você somou " + str(pontuacao) + " pontos e")
    print("seu risco cardiovascular é médio habitual.")
elif pontuacao >= 25 and pontuacao <= 31:
    print("Você somou " + str(pontuacao) + " pontos e")
    print("seu risco cardiovascular é moderado.")
    print("Tome mais cuidado!!!")
elif pontuacao >= 32 and pontuacao <= 40:
    print("Você somou " + str(pontuacao) + " pontos e")
    print("seu risco cardiovascular é perigoso.")
    print("Tome mais cuidado e procure um médico!!!")
elif pontuacao >= 41:
    print("Você somou " + str(pontuacao) + " pontos e")
    print("seu risco cardiovascular é de altíssmo perigo.")
    print("Procure um médico urgentemente!!!")






