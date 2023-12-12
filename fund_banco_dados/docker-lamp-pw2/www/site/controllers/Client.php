<?php

class Client {
    public function register () {
        require_once('views/templates/header.php');
        require_once('views/client/register.php');
        require_once('views/templates/footer.php');
    }

    public function registerView () {

        $arrayStack = array();
        if (isset($_POST['front'])) {
            array_push($arrayStack, $_POST['front']);
        }

        if (isset($_POST['back'])) {
            array_push($arrayStack, $_POST['back']);
        }

        if (isset($_POST['devops'])) {
            array_push($arrayStack, $_POST['devops']);
        }

        if (isset($_POST['data'])) {
            array_push($arrayStack, $_POST['data']);
        }

        $arrayClient = array(
            'name' => $_POST['name'],
            'phone' => $_POST['phone'],
            'email' => $_POST['email'],
            'password' => $_POST['password'],
            'gender' => $_POST['gender'],
            'stack' => $arrayStack,
            'trabalhando' => $_POST['working'],
            'faixaIdade' => $_POST['age'],
            'objetivo' => $_POST['objective'],

        );

        require_once('views/templates/header.php');
        require_once('views/client/registerView.php');
        require_once('views/templates/footer.php');
    }

    public function listClients() {
        require_once('models/ClientModel.php');
        $ClientModel = new ClientModel();
        $result = $ClientModel -> getClients();

        $arrayClients = array();
        while ($line = $result -> fetch_assoc()) {
            array_push($arrayClients, $line);
        }

        require_once('views/templates/header.php');
        require_once('views/client/clientData.php');
        require_once('views/templates/footer.php');
    }

}

?>