<!DOCTYPE html>
<html lang="pt-bt">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Revisão html, css e js</title>
    <!-- JQUERY -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
    <!-- BOOTSTRAP -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="assets/css/style.css">
    <script src="assets/js/script.js"></script>
</head>
<body>


    <header class="p-5 bg-primary text-white text-center">
        <h1>Altos Site</h1>
    </header>

    <div class="container-fluid">
        <div class="row">            
            <nav class="col-md-3 p-3">
                <h2>Altos Menu</h2>
                <ul class="nav flex-column">
                    <li class="nav-item">
                        <a class="nav-link" href="?controller=site&action=home" id="menuHome">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="?controller=site&action=produtos" id="menuProdutos">Produtos</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="?controller=site&action=contatos" id="menuContatos">Contatos</a>
                </ul>
                <h2>Clientes</h2>
                <ul class="nav flex-column">
                    <li class="nav-item">
                        <a class="nav-link" href="?controller=client&action=register" id="menuClientesRegister">Registro</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="?controller=client&action=listClients" id="menuClientesList">Lista de Clientes</a>
                    </li>
                </ul>
            </nav>

            <section class="col-md-9 p-3">