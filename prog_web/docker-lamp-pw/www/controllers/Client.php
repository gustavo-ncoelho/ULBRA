<?php

class Client{

    public function register(){
        require_once('views/templates/header.php');
        require_once('views/client/register.php');
        require_once('views/templates/footer.php');
    }

    public function registerView(){
        $arrayClient = array(
            'name' => $_POST['name'],
            'email' => $_POST['email']
        );

        var_dump($arrayClient);
    }


}


?>