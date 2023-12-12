def dividir(a, b):
    quociente = a // b
    resto = a % b
    return quociente, resto
resultadoQuociente, resultadoResto = dividir(15,2)
print(resultadoResto,resultadoQuociente)
