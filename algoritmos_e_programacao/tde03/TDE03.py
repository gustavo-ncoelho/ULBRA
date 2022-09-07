## 1 ##


# preço = float(input("Insira o preço de fábrica do computador"))
 
# imposto = preço*0.3
# revenda = preço*0.1
 
# print("O preço de mercado do computador será de R$" + str(preço+imposto+revenda))


## 2 ##


# print("Insira três números inteiros: ")
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())

# print("Os números inseridos foram: " + str(n1) + ", " + str(n2) + " e " + str(n3))
# print("E o resultado da média dos três números é: " + str((n1+n2+n3)/3))


## 3 ##


# time = float(input("Digite em minutos o tempo da viagem: "))
# speed = float(input("Digite em Km/h a velocidade média da viagem: "))

# time = time/60
# dist = time*speed

# print("O consumo de combustível foi de " + str(dist/12) + " Litros")


## 4 ##


# print("Digite dois números inteiros: ")
# n1 = int(input())
# n2 = int(input())

# print("O quociente da divisão do primeiro número pelo segundo é: " + str(n1/n2))
# print("O resto desta divisão é: " + str(n1%n2))


## 5 ##


# print("Digite três números reais: ")
# n1 = float(input())
# n2 = float(input())
# n3 = float(input())

# print("A média dos números é: " + str((n1+n2+n3)/3))


## 6 ##


# print("Digite três números inteiros: ")
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# mult = n1*n2*n3
# soma = n1+n2+n3
# subtr = n1-n2-n3

# print("O resultado da multiplicação dos números é: " + str(mult))
# print("O resultado da soma dos números é: " + str(soma))
# print("O resultado da subtração dos números é: " + str(subtr))
# print("O resultado da soma de todos os outros resultados é :" + str(mult+soma+subtr))


## 7 ##


# print("Digite 5 valores inteiros: ")
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# n4 = int(input())
# n5 = int(input())

# print("A média aritmética dos números é: " + str((n1+n2+n3+n4+n5)/5))


## 8 ##


# from math import pi
# import math


# raio = float(input("Insira o raio da base do cilindro em metros: "))
# height = float (input("Insira a altura/comprimento do cilindro em metros: "))

# area_base = pi*(raio**2)
# area_alt = (2*pi)*raio*height
# total_area = area_base+area_alt

# litros_tinta = math.ceil(total_area/3)

# latas_tinta = math.ceil(litros_tinta/5)

# price = latas_tinta*150.00

# print("Para pintar toda a área interna deste cilindro serão necessárias " + str(latas_tinta) + " latas de tinta")
# print("Totalizando um valor de R$" + str(price))


## 9 ##


# preco_fabrica = float(input("Digite o preço de fábrica do computador: "))

# imposto = preco_fabrica*0.45
# revenda = preco_fabrica*0.28

# print("O preço final do computador será de R$" + str(imposto+revenda+preco_fabrica))


## 10 ##


# num = int(input("Digite o número do funcionário: "))
# sal = float(input("Digite o salário fixo: "))
# num_carros = float(input("Digite a quantidade de carros vendidos no mês: "))
# valor_pcarro = float(input("Digite o valor ganho por carro vendido: "))

# sal_final = sal + (num_carros*valor_pcarro)

# print("O funcionário número " + str(num) + " tem salário mensal de R$" + str(sal_final))

















