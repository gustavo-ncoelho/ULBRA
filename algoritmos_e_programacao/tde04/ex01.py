print("Digite dois números aleatórios e diferentes: ")
n1 = float(input())
n2 = float(input())

if n1 > n2:
    print("O maior número somado a 100 terá como resultado: " + str(int(n1+100)))
elif n2 > n1:
    print("O maior número somado a 100 terá como resultado: " + str(int(n2+100)))
elif n2 == n1:
    print("Os números não são diferentes, tente denovo!!!")
