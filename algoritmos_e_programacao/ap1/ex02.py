num_cigarros = int(input("Digite quantos cigarros em média você consome por dia: "))
tempo_meses = int(input("Digite há quanto tempo você fuma (em meses): "))

tempo_dias = tempo_meses*30
cigarros_total = num_cigarros*tempo_dias
tempo_vida = cigarros_total*15
tempo_vida = tempo_vida/1440

if tempo_dias <= 90:
    print("Você ja perdeu " + str(tempo_vida) + " dias de vida e possui dentes amarelos")
elif tempo_dias > 90 and tempo_dias <= 365:
    print("Você ja perdeu " + str(tempo_vida) + " dias de vida e possui perda de paladar e respiração comprometida")
elif tempo_dias > 365:
    print("Você ja perdeu " + str(tempo_vida) + " dias de vida e está com o pulmão comprometido")

