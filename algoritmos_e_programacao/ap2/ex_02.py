condicaoGeral = 0

while condicaoGeral != "n":
    condicao = False

    while condicao == False:
        condSimOuNao = 0
        print("Digite as três medidas do triângulo desejado:")
        a = float(input())
        b = float(input())
        c = float(input())
        if a < b + c and b < a + c and c < b + a:
            condicao = True
        else:
            print("As medidas não formam um triângulo, deseja tentar novamente ?")
            while condSimOuNao == 0:
                print("Digite s para sim e n para não:")
                simOuNao = input()
                if simOuNao == "s":
                    condSimOuNao = 1
                elif simOuNao == "n":
                    condSimOuNao = 2
                else:
                    continue
            print("----------------------------------")
        if condSimOuNao == 1:
            continue
        else:
            break

    cateto1 = 0
    cateto2 = 0
    hipotenusa = 0
    area = 0
    perimetro = 0

    if a > b and a > c:
        hipotenusa = a
        cateto1 = b
        cateto2 = c
    elif b > a and b > c:
        hipotenusa = b
        cateto1 = a
        cateto2 = c
    elif c > a and c > b:
        hipotenusa = c
        cateto1 = b
        cateto2 = a

    area = (cateto1 * cateto2) / 2
    perimetro = hipotenusa + cateto1 + cateto2

    print(f"Os valores digitados foram {a}, {b} e {c}")
    print(f"A área do triângulo é de {area}")
    print(f"O perímetro do triângulo é de {perimetro}")

    print("###################################################")

    while True:
        print("Deseja realizar outra operação ? Digite s para sim ou n para não")
        condicaoGeral = input()
        if condicaoGeral == "s":
            break
        elif condicaoGeral == "n":
            break
        else:
            continue

