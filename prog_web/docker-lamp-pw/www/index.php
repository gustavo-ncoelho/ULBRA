<?php

    //?page=home
    //?controller=site&action=home

    if(!isset($_GET['controller'])){
        //pagina inicial
    }else{
        switch ($_REQUEST){
            case 'site':
                
                if(isset($_GET['action'])){
                    //resposta padrao para o site
                }else{
                    switch ($_REQUEST['action']){
                        case home:
                                //chama métodos home
                            break;
                            
                        case produtos:
                                //chama métodos produtos
                            break;

                        case contatos:
                                //chama métodos contatos
                            break;
                    }
                }
                
            break;
            case 'clients':

        }
    }

?>

       