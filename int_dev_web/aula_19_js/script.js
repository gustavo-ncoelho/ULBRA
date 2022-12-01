// parte 1 exercicio

alert('alo mundo')

var valor
valor = prompt('digite um numero')
valor = parseFloat(valor)

if(valor<10) {
    alert(valor +'Valor é menor que 10')
}else if(valor == 10){
    alert('valor é 10')
}else{
    alert(valor +'0 valor é maior que 10')
}

// parte 2

var valor3 = parseFloat(prompt('Digite o primeiro valor'))
var valor4 = parseFloat(prompt('Digite o segundo valor'))

var resultado1 = valor3+valor4

alert('A soma dos valores é ' + resultado1)

// parte 3

var valor5 = parseFloatprompt(prompt('Digite o primeiro valor'))
var operacao = prompt('digite a operação(+, -, * ou /')
var valor6 = parseFloatprompt(prompt('Digite o segundo valor'))
var resultado2

switch(operacao){
    case'+':
        resultado2 = valor5 + valor6
    break
    case'-':
        resultado2 = valor5 - valor6
    break
    case'*':
        resultado2 = valor5 * valor6
    break
    case'/':
        resultado2 = valor5 / valor6
    break
    default:
        alert('Operação não foi identificada')
    break
}

alert('O resultado da operação é '+ resultado2)

// parte 4

var nome = prompt('Digite o nome')
var n = parseInt(prompt('Digite o numero de vezes para repetir'))

for(var i = 0; i <= n; i++){
    alert(nome)
}

// parte 5

var dados = []

dados[0] = prompt('Digite seu nome')
dados[1] = prompt('Digite seu e-mail')
dados[2] = prompt('Digite seu indereço')

console.log(dados)

// parte 5.1

var pessoa = {}

pessoa.nome = prompt('Digite seu nome')
pessoa.endereco = prompt('Digite seu endereço')
pessoa.email = prompt('Digite seu e-mail')

alert(pessoa.nome)

console.log(pessoa)