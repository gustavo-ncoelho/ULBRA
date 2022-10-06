frutas = ["maçã","uva","limão"]

for x in range(3):
    print(frutas[x])

print("------------------------------")

for fruta in frutas:
    print(fruta)

print("------------------------------")

for i,fruta in enumerate(frutas):
    print(i,fruta)

print("------------------------------")

frutas = ["maçã","uva","melão","limão"]

for fruta in frutas:
    if fruta == "melão":
        print("Oba tem melão!!!")
        break
    else:
        print("Não é melão")
else:
    print("Não tem melão :(")