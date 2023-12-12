<?php

class ClientController{

    var $ClientModel;

    public function __construct(){
        require_once('models/ClientModel.php');
        $this -> ClientModel = new ClientModel();
    }

    public function listClients(){
        $result = $this -> ClientModel -> listClients();
        $arrayClients = array();
        while($line = $result -> fetch_assoc()){
            array_push($arrayClients, $line);
        }
        header('Content-Type: application/json');
        echo(json_encode($arrayClients));
    }

    public function consultClient($idClient){
        $result = $this -> ClientModel -> consultClient($idClient);

        if($arrayClient = $result->fetch_assoc()){
            header('Content-Type: application/json');
            echo(json_encode($arrayClient));
        }

    }

    public function insertClient(){
        $arrayClient = (array) json_decode(file_get_contents("php://input"));
        $idClient = $this -> ClientModel -> insertClient($arrayClient);
        header('Content-Type: application/json');
        echo('
            {
                "status" : "1",
                "message" : "Cliente Inserido"
            }
        ');
    }

    public function updateClient($idClient){
        $arrayClient = (array) json_decode(file_get_contents("php://input"));
        $this -> ClientModel -> updateClient($idClient, $arrayClient);
        header('Content-Type: application/json');
        echo('
            {
                "status" : "2",
                "message" : "Cliente Alterado"
            }
        ');
    }

    public function deleteClient($idClient){
        $this -> ClientModel -> deleteClient($idClient);
        header('Content-Type: application/json');
        echo('
            {
                "status" : "3",
                "message" : "Cliente Deletado"
            }
        ');
    }
}

?>