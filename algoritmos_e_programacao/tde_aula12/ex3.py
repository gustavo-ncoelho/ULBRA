num1 = int(input("Digite um número inteiro:\n"))
num2 = int(input("Digite outro número inteiro:\n"))

if num1 > num2:
    for num2 in range(num1):
        if num2%2 != 0:
            print(num2)
        else:
            continue
elif num2 > num1:
    for num1 in range(num2):
        if num1%2 != 0:
            print(num1)
        else:
            continue

print("-------------------------")

num3 = int(input("Digite um número inteiro:\n"))
num4 = int(input("Digite outro número inteiro:\n"))

if num3 > num4:
    while num4 < num3:
        num4 += 1
        if num4%2 != 0:
            print(num4)
        else:
            continue
elif num4 > num3:
    while num3 < num4:
        num3 += 1
        if num3%2 != 0:
            print(num3)
        else:
            continue
