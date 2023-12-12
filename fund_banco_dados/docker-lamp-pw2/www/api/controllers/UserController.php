<?php
class UserController{

    public function validateLogin(){
        $userData = (array)json_decode(file_get_contents("php://input"));

        $userName = $userData["userName"];
        $password = $userData["password"];

        require_once('models/UserModel.php');
        $UserModel = new UserModel();

        $result = $UserModel -> consultUser($userName);

        if($user = $result -> fetch_assoc()){
            if($password == $user['password']){
                $this -> createJWT($user);
            }else{
                echo 'senha inválida';
            }
        }else{
            echo 'usuário não existente';
        }
    }

    public function createJWT($user){
        $header = [
            'alg' => 'HS256',
            'typ' => 'JWT'
        ];
        $header = json_encode($header);
        $header = base64_encode($header);
        $header = str_replace(['+', '/', '='], ['-', '_', ''], $header);

        $payload = [
            'iss' => 'localhost',
            'name' => $user['name'],
            'user' => $user['user'],
            'adm' => $user['admin']
        ];
        $payload = json_encode($payload);
        $payload = base64_encode($payload);
        $payload = str_replace(['+', '/', '='], ['-', '_', ''], $payload);

        $signature = hash_hmac('sha256', "$header.$payload",'minha-senha',true);
        $signature = base64_encode($signature);
        $signature = str_replace(['+', '/', '='], ['-', '_', ''], $signature);

        $token = $header . "." . $payload . "." . $signature;

        header('Content-Type application/json');
        echo ('{"acess":"true","token":"'.$token.'"}');
    }

    public function isAdmin(){
        $header = apache_request_headers();
        $token = $header['Authorization'];
        $token = str_replace("Bearer ", "", $token);

        $part = explode(".",$token);
        $header = $part[0];
        $payload = $part[1];
        $signature = $part[2];

        $valid = hash_hmac('sha256', "$header.$payload",'minha-senha',true);
        $valid = base64_encode($valid);
        $valid = str_replace(['+', '/', '='], ['-', '_', ''], $valid);

        if($signature == $valid){
            $payload = str_replace(['-', '_', ''], ['+', '/', '='], $payload);
            $payload = base64_decode($payload);
            $payload = json_decode($payload);
            if($payload -> adm){
                return true;
            }else{
                header('Content-Type: application/json');
                echo ('{"acess":"false","message":"Nível de acesso inválido"}');
                return false;
            }
        }else{
            header('Content-Type: application/json');
            echo ('{"acess":"false","message":"Token inválido"}');
            return false;
        }
    }
}
?>