print("Digite 1 para: Conversão de Pés para Metros")
print("Digite 2 para: Conversão de Polegadas para Metros")
print("Digite 3 para: Conversão de Jardas para Metros")

n = int(input())

if n >= 1 and n <= 3:
    medida = float(input("Digite a medida a ser convertida: "))
else:
    print("Valor inválido, tente novamente!!!")

if n == 1:
    medida_final = medida/3.281
    print("Resultado: " + str(round(medida_final,2)) + "m")
elif n == 2:
    medida_final = medida/39.97
    print("Resultado: " + str(round(medida_final,2)) + "m")
elif n == 3:
    medida_final = medida/1.094
    print("Resultado: " + str(round(medida_final,2)) + "m")