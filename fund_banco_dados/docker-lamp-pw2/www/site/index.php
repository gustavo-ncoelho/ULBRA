<?php

    if (!isset($_GET['controller'])) {
        require_once('controllers/Site.php');
        $Site = new Site();
        $Site -> home();
    }
    else {
        switch ($_REQUEST['controller']) {
            case 'site':
                require_once('controllers/Site.php');
                $Site = new Site();

                if (!isset($_GET['action'])) {
                    $Site -> home();
                }
                else {
                    switch ($_REQUEST['action']) {
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
                $Client = new Client;

                if (!isset($_GET['action'])) {
                    $Client-> register();
                }
                else {
                    switch ($_REQUEST['action']) {
                        case 'register':
                            $Client -> register();
                            break;

                        case 'registerView':
                            $Client -> registerView();
                            break;

                        case 'listClients':
                            $Client -> listClients();
                            break;

                        default:
                            $Client -> register();
                            break;
                    }
                }
                break;

            default:
                require_once('controllers/Site.php');
                $Site = new Site();
                $Site -> home();
                break;
        }
    }
?>