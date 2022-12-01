function calculadora(){
    var numero1 = parseFloat(document.getElementById('valor1').value)
    var numero2 = parseFloat(document.getElementById('valor2').value)
    var operacao = document.getElementById('operacao').value
    var resultado


    switch (operacao) {
        case '+':
            resultado = numero1 + numero2
            break;
        
        case '-':
            resultado = numero1 - numero2
            break;
        
        case '/':
            resultado = numero1 / numero2
            break;

        case '*':
            resultado = numero1 * numero2
            break;
    }
    document.getElementById('resultado1').innerHTML = 'Resultado é: ' + resultado
}