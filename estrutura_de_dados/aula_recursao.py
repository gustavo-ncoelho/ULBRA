def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
num = int(input('Digite um número inteiro para saber seu fatorial: '))

print(fatorial(num))