<?php

Class ClientModel {

    public function getClients() {
        require_once('db/ConnectClass.php');
        $ConnectClass = new ConnectClass();
        $ConnectClass -> openConnection();

        $conn = $ConnectClass -> getConnection();
        $sql = "SELECT * FROM clients";
        $result = $conn -> query($sql);

        $conn -> close();
        return $result;
    }
}

?>