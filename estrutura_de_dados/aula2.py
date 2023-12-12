try:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
except ValueError:
    print("Número inválido")
else:
    print("Operação concluída")
finally:
    print("Fim da execução")