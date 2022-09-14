conta = int(input("Digite o número da sua conta bancária: "))
saldo = float(input("Digite o seu saldo: "))

if saldo < 0:
    print("Conta estourada")
elif saldo > 0:
    print("Conta normal")
elif saldo == 0:
    print("Sem saldo")