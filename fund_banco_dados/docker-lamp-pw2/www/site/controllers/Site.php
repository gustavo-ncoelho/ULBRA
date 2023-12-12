<?php

    class Site{
        public function home(){
            require_once('views/templates/header.php');
            require_once('views/pages/home.php');
            require_once('views/templates/footer.php');
        }

        public function produtos(){
            require_once('views/templates/header.php');
            require_once('views/pages/produtos.php');
            require_once('views/templates/footer.php');            
        }

        public function contatos(){
            require_once('views/templates/header.php');
            require_once('views/pages/contatos.php');
            require_once('views/templates/footer.php');
        }
    }

    

?>