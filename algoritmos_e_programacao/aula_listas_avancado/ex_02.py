listaNomes = []
cond = False

print("Digite diversos nomes e para encerrar a lista digite fim")
while cond == False:
    nome = input()
    if nome == "fim":
        cond = True
    else:
        listaNomes.append(nome)

print(listaNomes)