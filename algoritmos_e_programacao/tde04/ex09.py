print("Digite três números: ")

n1 = float(input())
n2 = float(input())
n3 = float(input())

if n1 > n2 and n1 > n3:
    print("O número " + str(n1) + " é o maior dos três")
elif n2 > n3 and n2 > n1:
    print("O número " + str(n2) + " é o maior dos três")
elif n3 > n2 and n3 > n1:
    print("O número " + str(n3) + " é o maior dos três")