print("Digite dois números diferentes: ")
n1 = float(input())
n2 = float(input())

if n1 > n2:
    print("A diferença do maior pelo menor é " + str(n1-n2))
elif n1 < n2:
    print("A diferença do maior pelo menor é " + str(n2-n1))