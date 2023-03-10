$(document).ready(function(){

    $("#menuHome").click(function(){
        $("section").load("pages/home.html");
    });

    $("#menuProdutos").click(function(){
        $("section").load("pages/produtos.html");
    });

    $("#menuContatos").click(function(){
        $("section").load("pages/contatos.html");
    });

  });