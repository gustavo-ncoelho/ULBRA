<?php

    ini_set('display_errors', 1);
    ini_set('display_startup_errors',1);
    error_reporting(E_ALL);

    if(!isset($_GET['controller'])){
        require_once('controllers/Site.php');
        $Site = new Site();
        $Site -> home();
    }else{
        switch($_REQUEST['controller']){
            case 'site':
                require_once('controllers/Site.php');
                $Site = new Site();
                if(!isset($_GET['action'])){
                    $Site -> home();
                }else{
                    switch($_REQUEST['action']){
                        case 'home':
                            $Site -> home();
                        break;

                        case 'produtos':
                            $Site -> produtos();
                        break;

                        case 'contatos':
                            $Site -> contatos();
                        break;

                        default:
                            $Site -> home();
                        break;
                    }
                }
            break;

            case 'client':
                require_once('controllers/Client.php');
                $Client = new Client();
                if(!isset($_GET['action'])){

                }else{
                    switch($_REQUEST['action']){
                        case 'register':
                            $Client -> register();
                        break;

                        case 'registerView':
                            $Client -> registerView();
                        break;
                    }
                }    
            break;

            default:
                require_once('views/templates/header.php');
                require_once('views/pages/home.php');
                require_once('views/templates/footer.php');
            break;               
        }
    }

?>

       