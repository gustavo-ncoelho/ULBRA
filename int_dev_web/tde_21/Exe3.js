function verificaMaior() {
    var numeros = document.getElementById('numeros').value
    numeros = numeros.split(',')
    var maior = 0
    for(i=0; i < numeros.length; i++){
        var numeroAtual = parseFloat(numeros[i])
        if(maior < numeroAtual)
        maior = numeroAtual
    }
    document.getElementById('maiorNumero').innerHTML =  'O maior valor é: ' + maior
}