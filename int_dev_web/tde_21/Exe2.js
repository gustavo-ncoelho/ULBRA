function calculoConta(){
    var quantiedade = parseFloat(document.getElementById('quantiedade').value)
    var valor = parseFloat(document.getElementById('valor').value)
    var conta

    if(quantiedade <=100){
        conta = quantiedade * valor
    }else if (quantiedade > 100 && quantiedade <=200){
        conta = (quantiedade*valor) * 1.25
    }else{
        conta= (quantiedade * valor) * 1.25
    }
    
    document.getElementById('resultado2').innerHTML =   'O valor da conta é: ' + conta
}