height = float(input("Digite sua altura: "))

print("Escolha seu gênero")
print("Digite M para Masculo e F para Feminino: ")

gender = input()

if gender == "M":
    peso_ideal = ((72.2*height)-58)
    print("Seu peso ideal é de : " + str(round(peso_ideal,2)) + "Kg")
elif gender == "F":
    peso_ideal = ((62.1*height)-44.7)
    print("Seu peso ideal é de: " + str(round(peso_ideal,2)) + "Kg")
elif gender != "M" or gender != "F":
    print("Erro de syntax, tente novamente!!!")