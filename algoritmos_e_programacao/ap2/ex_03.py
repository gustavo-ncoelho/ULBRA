num = int(input('Digite o valor que deseja sacar: '))

notas100 = int(num / 100)
num = num - (notas100*100)
    
notas50 = int(num/50)
num = num - (notas50*50)

notas10 = int(num/10)
num = num - (notas10*10)

notas5 = int(num/5)
num= num - (notas5*5)

notas2 = int(num/2)
num = num - (notas2*2)

notas1 = num
    
print(f'Notas R$100,00: {notas100}')
print(f'Notas R$ 50,00: {notas50}')
print(f'Notas R$ 10,00: {notas10}')
print(f'Notas R$  5,00: {notas5}')
print(f'Notas R$  2,00: {notas2}')
print(f'Notas R$  1,00: {notas1}')