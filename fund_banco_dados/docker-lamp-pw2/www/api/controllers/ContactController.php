<?php
    class ContactController{

        var $ContactModel;

        public function __construct(){
            require_once('models/ContactModel.php');
            $this -> ContactModel = new ContactModel();
        }

        public function listContacts(){
            $result = $this -> ContactModel -> listContacts();
            $arrayContacts = array();
            while($line = $result -> fetch_assoc()){
                array_push($arrayContacts, $line);
            }
            header('Content-Type: application/json');
            echo(json_encode($arrayContacts));
        }
    
        public function consultContact($idContact){
            $result = $this -> ContactModel -> consultContact($idContact);
    
            if($ArrayContact = $result -> fetch_assoc()){
                header('Content-Type: application/json');
                echo(json_encode($ArrayContact));
            }
    
        }
    
        public function insertContact(){
            $ArrayContact = (array)json_decode(file_get_contents("php://input"));
            $idContact = $this -> ContactModel -> insertContact($ArrayContact);
            header('Content-Type: application/json');
            echo('
                {
                    "status" : "1",
                    "message" : "Contato Inserido"
                }
            ');
        }
    }
?>