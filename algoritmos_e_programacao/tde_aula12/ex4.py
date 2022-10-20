soma = 0

for x in range(10):
    nota_aluno = float(input("Digite a nota do aluno:\n"))
    soma += nota_aluno

media_total = soma/10

print(f"\nA média das notas dos alunos é de: {media_total}")


print("-------------------------")


notas = []
soma = 0

while len(notas) != 10:
    notas.append(float(input("Digite a nota do aluno:\n")))

for nota in notas:
    soma += nota

media = soma/len(notas)

print(f"\nA média das notas dos alunos é de: {media}")


