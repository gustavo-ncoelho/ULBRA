<?php

class ClientController{

    var $ClientModel;

    public function __construct(){
        if(!isset($_SESSION['user'])){
            header('Location:?controller=main&action=login');
        }
        require_once('models/ClientModel.php');  
        $this -> ClientModel = new ClientModel();
    }

    public function listClients(){
        $result = $this -> ClientModel -> listClients();
        $arrayClients = array();
        while($line = $result -> fetch_assoc()){
            array_push($arrayClients, $line);
        }

        require_once('views/templates/header.php');
        require_once('views/client/listClients.php');
        require_once('views/templates/footer.php');
       
    }

    public function detailsClient($idClient){
        $result = $this -> ClientModel -> consultClient($idClient);

        if($arrayClient = $result->fetch_assoc()){
            require_once('views/templates/header.php');
            require_once('views/client/detailsClient.php');
            require_once('views/templates/footer.php');
        }

    }

    public function insertClient(){
        require_once('views/templates/header.php');
        require_once('views/client/insertClient.php');
        require_once('views/templates/footer.php');
    }

    public function insertClientAction(){
        $arrayClient = array(
            'name' => $_POST['name'],
            'email' => $_POST['email'],
            'phone' => $_POST['phone'],
            'address' => $_POST['address']
        );
        $idClient = $this -> ClientModel -> insertClient($arrayClient);
        
        if(isset($_FILES['photo']) && $_FILES['photo']['name'] != ''){
            $this -> savePhoto($idClient);
        }
        header('Location:?controller=client&action=listClients');
    }

    public function updateClient($idClient){
        $result = $this -> ClientModel -> consultClient($idClient);
        if($arrayClient = $result->fetch_assoc()){
            require_once('views/templates/header.php');
            require_once('views/client/updateClient.php');
            require_once('views/templates/footer.php');
        }
    }

    public function updateClientAction($idClient){
        $arrayClient = array(
            'name' => $_POST['name'],
            'email' => $_POST['email'],
            'phone' => $_POST['phone'],
            'address' => $_POST['address']
        );
        if(isset($_FILES['photo']) && $_FILES['photo']['name'] != ''){
            $this -> savePhoto($idClient);
        }
        $this -> ClientModel -> updateClient($idClient, $arrayClient);
        header('Location:?controller=client&action=listClients');
    }
    public function deleteClient($idClient){
        $this -> ClientModel -> deleteClient($idClient);
        $localFile = "assets/img/client/{$idClient}.jpg";
        
        if(is_file("assets/img/client/{$idClient}.jpg")){
            unlink($localFile);
        }
        header('Location:?controller=client&action=listClients');
    }

    public function savePhoto($idClient){     
        $foto_temp = $_FILES["photo"]["tmp_name"];	
        $foto_name = $_FILES["photo"]["name"];		
        $extensao = str_replace('.','',strrchr($foto_name, '.'));         
        $img = null;
        if ($extensao == 'jpg' || $extensao == 'jpeg') { 
            $img = imagecreatefromjpeg($foto_temp);
        } else if ($extensao == 'png') { 
            $img = imagecreatefrompng($foto_temp);
        } else if ($extensao == 'gif') { 
            $img = imagecreatefromgif($foto_temp); 
        }  else     
            $img = imagecreatefromjpeg($foto_temp); 
        
        $localFile = "assets/img/client/{$idClient}.jpg";
        imagejpeg($img, $localFile); 
    }
}

?>