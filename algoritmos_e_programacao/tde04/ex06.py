print("Digite três números inteiros: ")
n1 = int(input())
n2 = int(input())
n3 = int(input())

print("Número 1: " + str(n1))
print("Número 2: " + str(n2))
print("Número 3: " + str(n3))

if n1 >= 0:
    print("A raiz quadrada é " + str(n1**(1/2)))
else:
    print("O número ao quadrado é " + str(n1**2))

if n2 >= 10 and n2 <= 100:
    print("O NÚMERO ESTA ENTRE 10 E 100, INTERVALO PERMITIDO")
else:
    print("O NÚMERO NÃO ESTÁ ENTRE 10 E 100, INTERVALO NÃO PERMITIDO")

if n3 < n2:
    print("A diferença entre eles é de " + str(n2-n3))
else:
    print("A soma dos números é: " + str(n2+n3))