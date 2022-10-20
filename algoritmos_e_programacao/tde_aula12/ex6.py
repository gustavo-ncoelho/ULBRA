numbers = []

print("Digite 5 números quaisquer: ")
numbers.append(int(input()))
numbers.append(int(input()))
numbers.append(int(input()))
numbers.append(int(input()))
numbers.append(int(input()))

print("\nOs números são respectivamente:\n ")

for i in numbers:
    if i == 0:
        print("Nulo")
    elif i > 0:
        print("Positivo")
    else:
        print("Negativo")


print("\n-------------------------\n")

print("\nOs números são respectivamente:\n ")

x = 0

while x < 5:
    if numbers[x] == 0:
        print("Nulo")
    elif numbers[x] > 0:
        print("Positivo")
    else:
        print("Negativo")
    x = x+1
