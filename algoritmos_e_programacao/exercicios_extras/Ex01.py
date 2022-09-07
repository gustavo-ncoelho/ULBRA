print("C para F digite 1")
print("C para K digite 2")
print("K para F digite 3")
print("K para C digite 4")
print("F para K digite 5")
print("F para C digite 6")

n = int(input())

if n < 1 or n > 6:
    print("Comando inválido, tente novamente")
else:
    temp = float(input("Digie a temperatura: "))
    
if n == 1:
    print("A temperatura em F é: " + str(9/5*(temp)+32) + "ºF")
elif n == 2:
    print("A temperatura em K é: " + str(temp+273) +"K")
elif n == 3:
    print("A temperatura em F é: " + str((temp-273)*9/5+32) + "ºF")
elif n == 4:
    print("A temperatura em C é: " + str(temp-273)  + "ºC")   
elif n == 5:
    print("A temperatura em K é: " + str(5/9(temp-32)+273) + "K")
elif n == 6:
    print("A temperatura em C é: " + str(temp-32)*5/9 + "ºC")