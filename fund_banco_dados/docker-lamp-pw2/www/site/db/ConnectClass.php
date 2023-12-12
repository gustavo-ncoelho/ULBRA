<?php

Class ConnectClass {
    public $servername = "db";
    public $username = "root";
    public $password = "1q2w3e4r5t";
    public $dbname = "pw_exemple";

    var $conn;

    public function openConnection() {
        $this -> conn = new mysqli(
            $this -> servername,
            $this -> username,
            $this -> password,
            $this -> dbname
        );

        if ($this -> conn -> connect_error) {
            die("Connection to DB failed: " . $this -> conn -> connect_error);
        }
    }

    public function getConnection() {
        return $this -> conn;
    }
}


?>